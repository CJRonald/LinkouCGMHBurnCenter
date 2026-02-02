# 新聞稿資料夾 / News Folder

此資料夾用於存放燒燙傷中心的新聞稿檔案與相關圖片。

---

## 資料夾結構

每個新聞事件以獨立資料夾存放，包含新聞稿與相關照片。

```text
news/
├── 2024/                                    # 2024年
│   └── 20240910_DrFisher_Visiting/          # 事件資料夾
│       ├── 20240910_DrFisher.md             # 新聞稿內容
│       └── 01_GroupPhoto.jpg                # 活動照片
├── 2026/                                    # 2026年
│   └── 20260127_八仙塵爆十週年追思會/       # 事件資料夾
│       ├── 新聞稿.md                        # 新聞稿內容
│       ├── 01_活動現場.jpg                  # 活動照片
│       └── 02_貴賓合影.jpg                  # 活動照片
└── README.md                                # 本說明檔
```

---

## 命名規則

### 事件資料夾

- 格式：`YYYYMMDD_事件名稱`
- 範例：`20260127_八仙塵爆十週年追思會`、`20240910_DrFisher_Visiting`

### 新聞稿檔案

- 格式：`YYYYMMDD_事件名稱.md` 或 `新聞稿.md`
- 範例：`20240910_DrFisher.md`

### 照片檔案

- 格式：`序號_描述.jpg`
- 範例：
  - `01_活動現場.jpg`
  - `02_貴賓合影.jpg`
  - `03_追思儀式.jpg`

---

## 圖片規格建議

| 用途 | 建議尺寸 | 格式 |
|------|----------|------|
| 主視覺 | 1200 x 630 px | JPG |
| 內文配圖 | 800 x 600 px | JPG/PNG |
| 人物特寫 | 400 x 400 px | JPG |

---

## 新增新聞事件完整步驟

> **重要提醒**：新增一則新聞需同時更新多個檔案，請依照以下步驟逐一完成。

---

### 步驟 1：建立素材資料夾

在 `assets/news/YYYY/` 下建立事件資料夾：

```
assets/news/2026/20260127_事件名稱/
├── 新聞稿.md          # 新聞稿原始內容
├── 01_活動現場.jpg    # 活動照片
└── 02_貴賓合影.jpg    # 活動照片
```

---

### 步驟 2：建立 HTML 詳細頁（中英文）

在 `pages/news/YYYY/` 下建立詳細頁：

```
pages/news/2026/
├── news-20260127-event-name.html      # 中文版
└── news-20260127-event-name-en.html   # 英文版
```

**注意事項：**

- 可參考同資料夾內的現有頁面作為範本
- 注意相對路徑：從 `pages/news/YYYY/` 回溯使用 `../../../` 到根目錄

**路徑範例：**

```html
<!-- CSS/JS -->
<link rel="stylesheet" href="../../../assets/css/main.css">
<script src="../../../assets/js/main.js"></script>

<!-- Logo 和首頁連結 -->
<a href="../../../index.html" class="logo">
<img src="../../../assets/images/logos/CGMH Logo.svg">

<!-- 新聞列表頁連結 -->
<a href="../../news.html">最新消息</a>
<a href="../../news-en.html">News</a>

<!-- 同資料夾內的語言切換 -->
<a href="news-20260127-event-name-en.html">English</a>
<a href="news-20260127-event-name.html">中文</a>

<!-- 圖片 -->
<img src="../../../assets/news/2026/20260127_事件名稱/01_活動現場.jpg">
```

---

### 步驟 3：更新新聞列表頁

#### 中文版 `pages/news.html`

1. 在 `<!-- Filter Tabs -->` 區塊新增分類標籤（如需新增）
2. 在 `<!-- News Articles -->` 區塊新增新聞條目
3. 連結格式：`href="news/2026/news-20260127-event-name.html"`
4. 新聞按日期由新到舊排列

#### 英文版 `pages/news-en.html`

1. 同步更新英文版分類標籤
2. 新增對應的英文新聞條目
3. 連結格式：`href="news/2026/news-20260127-event-name-en.html"`

---

### 步驟 4：更新首頁新聞區（若為重要新聞）

若要在首頁顯示此新聞，需更新：

#### 中文版 `index.html`

- `<!-- Latest News Section -->` 區塊
- 連結格式：`href="pages/news/2026/news-20260127-event-name.html"`

#### 英文版 `index-en.html`

- `<!-- Latest News Section -->` 區塊
- 連結格式：`href="pages/news/2026/news-20260127-event-name-en.html"`

---

## 需要修改的檔案清單

新增一則新聞時，可能需要修改以下檔案：

| 檔案 | 用途 | 必須 |
|------|------|:----:|
| `assets/news/YYYY/事件資料夾/` | 素材資料夾 | ✅ |
| `pages/news/YYYY/news-YYYYMMDD-name.html` | 中文詳細頁 | ✅ |
| `pages/news/YYYY/news-YYYYMMDD-name-en.html` | 英文詳細頁 | ✅ |
| `pages/news.html` | 中文列表頁 | ✅ |
| `pages/news-en.html` | 英文列表頁 | ✅ |
| `index.html` | 中文首頁 | ⚪ |
| `index-en.html` | 英文首頁 | ⚪ |

> ⚪ = 選擇性（僅重要新聞需更新首頁）

---

## 資料夾結構總覽

```
LinkouCGMHBurnCenter/
├── assets/news/                    # 素材資料夾
│   ├── 2024/
│   │   └── 20240910_DrFisher_Visiting/
│   ├── 2025/
│   │   └── 20250927_長庚美容會議/
│   └── 2026/
│       └── 20260127_八仙塵爆十週年追思會/
│
├── pages/news/                     # 新聞詳細頁
│   ├── 2024/
│   │   ├── news-20240910-drfisher.html
│   │   └── news-20240910-drfisher-en.html
│   ├── 2025/
│   │   ├── news-20250927-cgac.html
│   │   └── news-20250927-cgac-en.html
│   └── 2026/
│       ├── news-20260127-formosa-memorial.html
│       └── news-20260127-formosa-memorial-en.html
│
├── pages/news.html                 # 新聞列表頁（中文）
├── pages/news-en.html              # 新聞列表頁（英文）
├── index.html                      # 首頁（中文）
└── index-en.html                   # 首頁（英文）
```

---

## 在 HTML 中引用圖片

從不同位置引用圖片的路徑：

| 來源位置 | 路徑格式 |
|----------|----------|
| `pages/news/2026/*.html` | `../../../assets/news/2026/事件/圖片.jpg` |
| `pages/news.html` | `../assets/news/2026/事件/圖片.jpg` |
| `index.html` | `assets/news/2026/事件/圖片.jpg` |
