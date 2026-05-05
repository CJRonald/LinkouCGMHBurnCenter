"""SEO metadata for each page in LinkouCGMHBurnCenter site.

Maps each HTML file path to its title, description, language pair,
and canonical URL. Used by inject_seo_meta.py to populate meta tags.
"""

DOMAIN = "https://cgmhburncenter.org"
SITE_NAME_ZH = "林口長庚燒傷中心"
SITE_NAME_EN = "Linkou CGMH Burn Center"
OG_IMAGE_ZH = f"{DOMAIN}/assets/images/og-image.png"
OG_IMAGE_EN = f"{DOMAIN}/assets/images/og-image-en.png"

# Each entry: relative path -> dict with title, description, lang, counterpart
PAGES = {
    "index.html": {
        "title": "林口長庚燒傷中心 - 專業燒燙傷醫療與研究",
        "description": "台灣最大規模燒燙傷治療中心，24小時急重症照護、疤痕重建與AI醫療研究",
        "lang": "zh_TW",
        "counterpart": "index-en.html",
    },
    "index-en.html": {
        "title": "Linkou CGMH Burn Center - Professional Burn Care & Research",
        "description": "Taiwan's largest burn treatment center: 24/7 critical care, scar reconstruction, AI medical research",
        "lang": "en_US",
        "counterpart": "index.html",
    },
    "pages/about.html": {
        "title": "關於我們 | 林口長庚燒傷中心",
        "description": "林口長庚燒傷中心成立沿革、願景與使命",
        "lang": "zh_TW",
        "counterpart": "pages/about-en.html",
    },
    "pages/about-en.html": {
        "title": "About Us | Linkou CGMH Burn Center",
        "description": "History, vision and mission of Linkou CGMH Burn Center",
        "lang": "en_US",
        "counterpart": "pages/about.html",
    },
    "pages/team.html": {
        "title": "醫療團隊 | 林口長庚燒傷中心",
        "description": "燒傷中心整形外科醫療團隊介紹",
        "lang": "zh_TW",
        "counterpart": "pages/team-en.html",
    },
    "pages/team-en.html": {
        "title": "Medical Team | Linkou CGMH Burn Center",
        "description": "Plastic surgery medical team of CGMH Burn Center",
        "lang": "en_US",
        "counterpart": "pages/team.html",
    },
    "pages/services.html": {
        "title": "醫療服務 | 林口長庚燒傷中心",
        "description": "燒燙傷急重症照護、疤痕重建、眼鼻整形與手外科服務",
        "lang": "zh_TW",
        "counterpart": "pages/services-en.html",
    },
    "pages/services-en.html": {
        "title": "Services | Linkou CGMH Burn Center",
        "description": "Burn critical care, scar reconstruction, facial and hand surgery",
        "lang": "en_US",
        "counterpart": "pages/services.html",
    },
    "pages/research.html": {
        "title": "研究領域 | 林口長庚燒傷中心",
        "description": "AI 醫療影像、創傷修復、3D 重建研究方向",
        "lang": "zh_TW",
        "counterpart": "pages/research-en.html",
    },
    "pages/research-en.html": {
        "title": "Research | Linkou CGMH Burn Center",
        "description": "AI medical imaging, wound healing, 3D reconstruction research",
        "lang": "en_US",
        "counterpart": "pages/research.html",
    },
    "pages/publications.html": {
        "title": "研究發表 | 林口長庚燒傷中心",
        "description": "期刊論文、研討會發表與研究成果",
        "lang": "zh_TW",
        "counterpart": "pages/publications-en.html",
    },
    "pages/publications-en.html": {
        "title": "Publications | Linkou CGMH Burn Center",
        "description": "Journal publications, conference presentations and research outcomes",
        "lang": "en_US",
        "counterpart": "pages/publications.html",
    },
    "pages/education.html": {
        "title": "教育訓練 | 林口長庚燒傷中心",
        "description": "住院醫師訓練、研究員計畫與國際交流",
        "lang": "zh_TW",
        "counterpart": "pages/education-en.html",
    },
    "pages/education-en.html": {
        "title": "Education | Linkou CGMH Burn Center",
        "description": "Resident training, fellowship programs and international exchange",
        "lang": "en_US",
        "counterpart": "pages/education.html",
    },
    "pages/news.html": {
        "title": "中心動態 | 林口長庚燒傷中心",
        "description": "燒傷中心最新消息、活動與獎項",
        "lang": "zh_TW",
        "counterpart": "pages/news-en.html",
    },
    "pages/news-en.html": {
        "title": "News | Linkou CGMH Burn Center",
        "description": "Latest news, events and awards",
        "lang": "en_US",
        "counterpart": "pages/news.html",
    },
    "pages/news/2024/news-20240910-drfisher.html": {
        "title": "Dr. Fisher 學術交流 | 林口長庚燒傷中心",
        "description": "國際學者 Dr. Fisher 來訪交流紀實",
        "lang": "zh_TW",
        "counterpart": "pages/news/2024/news-20240910-drfisher-en.html",
    },
    "pages/news/2024/news-20240910-drfisher-en.html": {
        "title": "Dr. Fisher Academic Exchange | CGMH Burn Center",
        "description": "International scholar Dr. Fisher visit highlights",
        "lang": "en_US",
        "counterpart": "pages/news/2024/news-20240910-drfisher.html",
    },
    "pages/news/2025/news-20250927-cgac.html": {
        "title": "CGAC 學術會議 | 林口長庚燒傷中心",
        "description": "2025 CGAC 學術會議報導",
        "lang": "zh_TW",
        "counterpart": "pages/news/2025/news-20250927-cgac-en.html",
    },
    "pages/news/2025/news-20250927-cgac-en.html": {
        "title": "CGAC Conference | CGMH Burn Center",
        "description": "2025 CGAC academic conference report",
        "lang": "en_US",
        "counterpart": "pages/news/2025/news-20250927-cgac.html",
    },
    "pages/news/2026/news-20260127-formosa-memorial.html": {
        "title": "八仙塵爆十週年 | 林口長庚燒傷中心",
        "description": "八仙塵爆事件十週年紀念與反思",
        "lang": "zh_TW",
        "counterpart": "pages/news/2026/news-20260127-formosa-memorial-en.html",
    },
    "pages/news/2026/news-20260127-formosa-memorial-en.html": {
        "title": "Formosa Memorial | CGMH Burn Center",
        "description": "Formosa Fun Coast fire 10th anniversary memorial",
        "lang": "en_US",
        "counterpart": "pages/news/2026/news-20260127-formosa-memorial.html",
    },
}


def canonical_url(rel_path: str) -> str:
    """Build canonical URL. index.html maps to root."""
    if rel_path == "index.html":
        return f"{DOMAIN}/"
    return f"{DOMAIN}/{rel_path}"


def og_image_for(lang: str) -> str:
    return OG_IMAGE_EN if lang == "en_US" else OG_IMAGE_ZH


def site_name_for(lang: str) -> str:
    return SITE_NAME_EN if lang == "en_US" else SITE_NAME_ZH
