"""Build sitemap.xml from PAGES mapping with hreflang annotations."""

import sys
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).parent))
from seo_metadata import PAGES, DOMAIN, canonical_url  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
TODAY = date.today().isoformat()

# Priority by page type
def priority_for(rel_path: str) -> str:
    if rel_path in ("index.html", "index-en.html"):
        return "1.0"
    if rel_path.startswith("pages/news/"):
        return "0.6"
    return "0.8"


def changefreq_for(rel_path: str) -> str:
    if rel_path.startswith("pages/news/"):
        return "yearly"
    return "monthly"


def build_url_entry(rel_path: str, meta: dict) -> str:
    loc = canonical_url(rel_path)
    counterpart_path = meta["counterpart"]
    counterpart_url = canonical_url(counterpart_path)
    lang = meta["lang"]

    if lang == "en_US":
        zh_url, en_url = counterpart_url, loc
    else:
        zh_url, en_url = loc, counterpart_url

    return f"""  <url>
    <loc>{escape(loc)}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{changefreq_for(rel_path)}</changefreq>
    <priority>{priority_for(rel_path)}</priority>
    <xhtml:link rel="alternate" hreflang="zh-TW" href="{escape(zh_url)}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{escape(en_url)}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{escape(zh_url)}"/>
  </url>"""


def main() -> int:
    entries = [build_url_entry(rel, meta) for rel, meta in PAGES.items()]
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(entries)}
</urlset>
"""
    out = REPO_ROOT / "sitemap.xml"
    out.write_text(xml, encoding="utf-8")
    print(f"Wrote {out} ({len(PAGES)} URLs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
