"""Inject SEO meta tags into all HTML pages.

For each page in seo_metadata.PAGES:
- Removes any existing canonical / hreflang / OG / Twitter meta tags
- Inserts the standardized set right before </head>
- Preserves existing <title>, charset, viewport, description, keywords

Note: BeautifulSoup's html.parser will normalize existing tags on first run
(attribute order alphabetized, self-closing slashes added, charset case folded).
This is expected and harmless — subsequent runs are byte-stable. Review the
first commit's diff with this in mind; the SEO additions are at the end of <head>.

Usage:
    python3 scripts/inject_seo_meta.py [--dry-run] [--file PATH]
"""

import argparse
import sys
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString

# Allow running as `python3 scripts/inject_seo_meta.py`
sys.path.insert(0, str(Path(__file__).parent))
from seo_metadata import (  # noqa: E402
    PAGES,
    canonical_url,
    og_image_for,
    site_name_for,
)

REPO_ROOT = Path(__file__).resolve().parent.parent

# Tag selectors we own and will replace each run (idempotent re-runs)
OWNED_SELECTORS = [
    {"name": "link", "attrs": {"rel": "canonical"}},
    {"name": "link", "attrs": {"rel": "alternate", "hreflang": True}},
    {"name": "meta", "attrs": {"property": lambda v: v and v.startswith("og:")}},
    {"name": "meta", "attrs": {"name": lambda v: v and v.startswith("twitter:")}},
]


def remove_owned_tags(soup: BeautifulSoup) -> None:
    head = soup.head
    if head is None:
        raise RuntimeError("HTML missing <head>")
    for sel in OWNED_SELECTORS:
        for tag in head.find_all(sel["name"], attrs=sel["attrs"]):
            # Remove the trailing whitespace-only text node we may have inserted
            next_sibling = tag.next_sibling
            if isinstance(next_sibling, NavigableString) and not next_sibling.strip():
                next_sibling.extract()
            tag.decompose()


def build_tags(soup: BeautifulSoup, rel_path: str, meta: dict) -> list:
    """Construct ordered list of new tags to insert."""
    canonical = canonical_url(rel_path)
    counterpart_path = meta["counterpart"]
    counterpart_url = canonical_url(counterpart_path)
    lang = meta["lang"]
    is_en = lang == "en_US"

    if is_en:
        zh_url = counterpart_url
        en_url = canonical
    else:
        zh_url = canonical
        en_url = counterpart_url

    tags = []

    # Canonical
    tags.append(soup.new_tag("link", rel="canonical", href=canonical))

    # hreflang (zh-TW, en, x-default)
    tags.append(soup.new_tag("link", rel="alternate", hreflang="zh-TW", href=zh_url))
    tags.append(soup.new_tag("link", rel="alternate", hreflang="en", href=en_url))
    tags.append(soup.new_tag("link", rel="alternate", hreflang="x-default", href=zh_url))

    # OpenGraph
    og_tags = [
        ("og:type", "website"),
        ("og:url", canonical),
        ("og:title", meta["title"]),
        ("og:description", meta["description"]),
        ("og:image", og_image_for(lang)),
        ("og:locale", lang),
        ("og:site_name", site_name_for(lang)),
    ]
    for prop, content in og_tags:
        t = soup.new_tag("meta")
        t.attrs["property"] = prop
        t.attrs["content"] = content
        tags.append(t)

    # Twitter Card
    twitter_tags = [
        ("twitter:card", "summary_large_image"),
        ("twitter:title", meta["title"]),
        ("twitter:description", meta["description"]),
        ("twitter:image", og_image_for(lang)),
    ]
    for name, content in twitter_tags:
        t = soup.new_tag("meta")
        t.attrs["name"] = name
        t.attrs["content"] = content
        tags.append(t)

    return tags


def process_file(rel_path: str, dry_run: bool = False) -> bool:
    abs_path = REPO_ROOT / rel_path
    if not abs_path.exists():
        print(f"  SKIP (missing): {rel_path}")
        return False

    meta = PAGES[rel_path]
    html = abs_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    if soup.head is None:
        print(f"  SKIP (no <head>): {rel_path}")
        return False

    remove_owned_tags(soup)
    new_tags = build_tags(soup, rel_path, meta)

    # Insert as last children of <head> (before closing tag)
    for tag in new_tags:
        soup.head.append(tag)
        # Preserve readable indentation
        soup.head.append("\n    ")

    if dry_run:
        print(f"  DRY-RUN: {rel_path} ({len(new_tags)} tags)")
        return True

    abs_path.write_text(str(soup), encoding="utf-8")
    print(f"  OK: {rel_path}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--file", help="Process single file (relative path)")
    args = parser.parse_args()

    targets = [args.file] if args.file else list(PAGES.keys())
    if args.file and args.file not in PAGES:
        print(f"ERROR: {args.file} not in PAGES mapping", file=sys.stderr)
        return 1

    print(f"Processing {len(targets)} file(s){' (dry-run)' if args.dry_run else ''}:")
    ok = 0
    for rel in targets:
        if process_file(rel, dry_run=args.dry_run):
            ok += 1
    print(f"\nDone: {ok}/{len(targets)} files updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
