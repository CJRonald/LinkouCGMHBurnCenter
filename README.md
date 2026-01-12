# 林口長庚燒燙傷中心網站
# Linkou CGMH Burn Center Website

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Language](https://img.shields.io/badge/language-zh--TW%20%7C%20EN-green.svg)

台灣最大規模燒燙傷治療中心官方網站，提供中英雙語介面。

Official website for Taiwan's largest burn treatment center, featuring bilingual (Chinese/English) interface.

---

## 🏥 關於本中心 | About

林口長庚燒燙傷中心由羅慧夫醫師於 1978 年創立，現擁有：
- **30 床**專業病房（21 床急症加護隔離病房 + 9 床亞急性燒傷病房）
- **2 間**獨立開刀房
- **10+ 位**主治醫師
- **24 小時**急診服務

---

## 📁 專案結構 | Project Structure

```
LinkouCGMHBurnCenter/
├── index.html              # 首頁（中文）
├── index-en.html           # 首頁（英文）
├── pages/                  # 子頁面
│   ├── about.html          # 關於我們
│   ├── about-en.html
│   ├── team.html           # 醫療團隊
│   ├── team-en.html
│   ├── services.html       # 服務項目
│   ├── services-en.html
│   ├── research.html       # 研究領域
│   ├── research-en.html
│   ├── publications.html   # 學術發表
│   ├── publications-en.html
│   ├── education.html      # 衛教資訊
│   ├── education-en.html
│   ├── news.html           # 最新消息
│   └── news-en.html
├── assets/
│   ├── css/
│   │   └── main.css        # 主要樣式表
│   ├── js/
│   │   └── main.js         # 主要腳本
│   ├── images/             # 圖片資源
│   └── publications/       # 出版物檔案
└── LICENSE                 # MIT 授權條款
```

---

## 🔧 技術架構 | Tech Stack

| 技術 | 說明 |
|------|------|
| HTML5 | 語意化標記 |
| CSS3 | 響應式設計 |
| JavaScript | 互動功能 |
| [Google Fonts](https://fonts.google.com/) | Noto Sans TC 字體 |
| [Font Awesome](https://fontawesome.com/) | 圖示庫 |

---

## 🚀 快速開始 | Getting Started

### 本地開發

1. 複製專案：
   ```bash
   git clone https://github.com/CJRonald/LinkouCGMHBurnCenter.git
   cd LinkouCGMHBurnCenter
   ```

2. 使用任意靜態檔案伺服器開啟：
   ```bash
   # 使用 Python
   python -m http.server 8080

   # 或使用 Node.js (npx)
   npx serve .

   # 或使用 VS Code Live Server 擴充功能
   ```

3. 開啟瀏覽器前往 `http://localhost:8080`

---

## 📱 功能特色 | Features

- ✅ **雙語支援** - 完整中英文介面
- ✅ **響應式設計** - 支援桌機、平板、手機
- ✅ **無障礙設計** - 語意化 HTML 結構
- ✅ **SEO 優化** - 完整的 meta 標籤

---

## 🏥 核心服務 | Core Services

1. **急重症燒燙傷照護** - 24 小時專責醫療團隊
2. **慢性疤痕重建** - 個人化重建手術與雷射治療
3. **眼鼻整形重建** - 顏面整形與功能重建
4. **手外科關節重建** - 顯微手術與關節重建

---

## 🔬 研究領域 | Research Areas

- **視覺驅動智慧燒燙傷分析** - AI 影像辨識技術
- **3D 列印個人化重建** - 客製化重建方案
- **客製伸指機轉重建** - 手部功能重建技術

---

## 📞 聯絡資訊 | Contact

- **Email**: cgmh.burncenter@gmail.com
- **電話**: +886-3-328-1200 ext. 3221
- **地址**: 桃園市龜山區復興街5號 醫學大樓二樓

---

## 📄 授權條款 | License

本專案採用 [MIT License](LICENSE) 授權。

Copyright © 2025 Chih-Jung Huang

---

## 🤝 貢獻指南 | Contributing

歡迎提交 Issue 或 Pull Request 來協助改善本網站。

1. Fork 本專案
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送至分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request
