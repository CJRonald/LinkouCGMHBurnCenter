# 學術發表 PDF 檔案資料夾

此資料夾用於存放林口長庚燒燙傷中心的學術發表相關 PDF 檔案。

## 資料夾結構

```
publications/
├── 2024/          # 2024年發表的期刊論文
├── 2023/          # 2023年發表的期刊論文
├── 2022/          # 2022年發表的期刊論文
├── patents/       # 專利技術相關文件
├── books/         # 專書著作與書籍章節
├── conferences/   # 會議發表與海報
└── README.md      # 本說明檔案
```

## 檔案命名規範

### 期刊論文
格式: `{主要關鍵字}_{年份}.pdf`

範例:
- `stack_te_technique_2024.pdf`
- `ai_burn_assessment_2024.pdf`
- `ml_inhalation_injury_2023.pdf`

### 專利文件
格式: `patent_{技術關鍵字}_{年份}.pdf`

範例:
- `patent_extensor_system_2024.pdf`
- `patent_ai_diagnosis_2023.pdf`

### 會議發表
格式: `conf_{會議縮寫}_{主題}_{年份}.pdf`

範例:
- `conf_isbi_scar_treatment_2024.pdf`
- `conf_aps_3d_printing_2023.pdf`

## 使用說明

1. **新增檔案時**：
   - 確認檔案格式為 PDF
   - 按照命名規範命名檔案
   - 放入對應的年份或類型資料夾
   - 更新 `publications-reference.md` 中的檔案路徑

2. **檔案大小限制**：
   - 建議單一 PDF 檔案不超過 10MB
   - 如有大型檔案，考慮壓縮或提供外部連結

3. **版權注意事項**：
   - 確保有權限上傳和分享檔案
   - 遵守期刊出版商的版權政策
   - 優先提供開放存取版本

## 網頁連結設定

在 HTML 頁面中的連結格式：
```html
<a href="../assets/publications/2024/stack_te_technique_2024.pdf" class="publication-link">
    <i class="fas fa-file-pdf"></i>
    PDF全文
</a>
```

## 維護指南

- 定期檢查檔案完整性
- 清理過舊或不再需要的檔案
- 確保檔案路徑與網頁連結一致
- 備份重要檔案到其他儲存位置

## 聯絡資訊

如有檔案管理相關問題，請聯絡：
- Email: cgmh.burncenter@gmail.com
- 電話: +886-3-328-1200 ext. 3221