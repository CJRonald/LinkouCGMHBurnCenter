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

## 新增新聞稿步驟

### 1. 建立事件資料夾

在對應年份資料夾下建立事件資料夾（如 `20260127_事件名稱`）

### 2. 新增新聞稿內容

將新聞稿存為 `YYYYMMDD_事件名稱.md` 或 `新聞稿.md`

### 3. 新增照片

將相關照片以 `序號_描述.jpg` 格式存入資料夾

### 4. 建立 HTML 詳細頁

在 `pages/` 資料夾建立對應的 HTML 頁面：

- 檔名格式：`news-YYYYMMDD-簡短名稱.html`
- 範例：`news-20240910-drfisher.html`
- 可參考現有頁面如 `news-20260127-formosa-memorial.html` 作為範本

### 5. 更新新聞列表頁（中文）

編輯 `pages/news.html`：

1. 在 `<!-- Filter Tabs -->` 區塊確認分類標籤存在（如需新增分類）
2. 在 `<!-- News Articles -->` 區塊新增新聞條目
3. 新聞按日期由新到舊排列

### 6. 更新新聞列表頁（英文）

編輯 `pages/news-en.html`：

1. 同步更新英文版分類標籤
2. 新增對應的英文新聞條目

---

## 在 HTML 中引用圖片

```html
<img src="../assets/news/2024/20240910_DrFisher_Visiting/01_GroupPhoto.jpg" alt="Dr. Fisher 與團隊合影">
```

---

## 相關頁面

| 頁面 | 路徑 |
|------|------|
| 新聞列表頁（中文） | `pages/news.html` |
| 新聞列表頁（英文） | `pages/news-en.html` |
| 新聞稿詳細頁 | `pages/news-YYYYMMDD-*.html` |

---

## 範例：新增 Dr. Fisher 參訪新聞

### 完成的檔案清單

1. ✅ `assets/news/2024/20240910_DrFisher_Visiting/20240910_DrFisher.md` - 新聞稿原始內容
2. ✅ `assets/news/2024/20240910_DrFisher_Visiting/01_GroupPhoto.jpg` - 活動照片
3. ✅ `pages/news-20240910-drfisher.html` - HTML 詳細頁
4. ✅ `pages/news.html` - 已新增新聞條目與「國際交流」分類
5. ✅ `pages/news-en.html` - 已新增英文新聞條目與「International Exchange」分類
