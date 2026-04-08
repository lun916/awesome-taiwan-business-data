# Awesome Taiwan Business Data

> 台灣公司、商業登記、政府標案、法律案件等公開資料的來源整理與查詢工具索引。

適合：開發者、研究人員、求職者、投資人、創業者、記者。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Data: OGDL 1.0](https://img.shields.io/badge/Data-OGDL%201.0-green.svg)](https://data.gov.tw/license)

## 背景

台灣有超過 200 萬家登記公司，相關資料散落在 經濟部、財政部、法務部、勞動部、食藥署、智慧財產局 等多個機關。雖然每個機關都有提供開放資料 API 或下載，但**整合查詢困難、欄位定義不一致**是長期痛點。

民間社群與政府都有提供查詢工具，本 repo 整理常用的資料來源與工具，方便開發者、研究人員、求職者使用。

---

## 📚 依資料類型查詢

### 🏢 公司基本資料（公司名稱、統編、負責人、資本額、地址）

| 來源 | 連結 | 說明 |
|---|---|---|
| 整合查詢工具 | [NowTo 商業通](https://biz.now.to/) | 整合 200 萬+ 家公司資料，含標案、訴訟、勞動違規等多源資料整合在單一頁面 |
| 政府原始資料 | [經濟部商工登記公示資料查詢](https://findbiz.nat.gov.tw/) | 經濟部商業司官方系統 |
| 政府開放資料 | [data.gov.tw 全國公司登記基本資料](https://data.gov.tw/dataset/9101) | 可下載 CSV，OGDL 1.0 授權 |

### 🏛️ 政府標案（招標、決標、得標廠商）

| 來源 | 連結 | 說明 |
|---|---|---|
| 線上查詢 | [NowTo 商業通 - 標案排行](https://biz.now.to/top/tenders) | 公司關聯標案查詢 |
| 政府原始系統 | [政府電子採購網](https://web.pcc.gov.tw/) | 行政院公共工程委員會 |
| 政府開放資料 | [data.gov.tw 政府採購公告資料](https://data.gov.tw/dataset/6056) | XML/JSON 格式 |

### ⚖️ 法律案件（民事、刑事、行政訴訟）

| 來源 | 連結 | 說明 |
|---|---|---|
| 公司關聯查詢 | [NowTo 商業通 - 訴訟排行](https://biz.now.to/top/lawsuits) | 以公司為索引的訴訟查詢 |
| 政府原始系統 | [司法院裁判書系統](https://judgment.judicial.gov.tw/) | 全文檢索 |

### 🏭 工廠登記

| 來源 | 連結 | 說明 |
|---|---|---|
| 政府原始系統 | [經濟部產業發展署工廠公示資料查詢系統](https://serv.gsn.gov.tw/) | 約 9 萬筆 |
| 政府開放資料 | [data.gov.tw 工廠校正及營運調查資料](https://data.gov.tw/dataset/9839) | CSV 格式 |

### 🍱 食品業者登錄與違規

| 來源 | 連結 | 說明 |
|---|---|---|
| 食品業者登錄 | [食藥署食品業者登錄平台](https://fadenbook.fda.gov.tw/) | 60 萬+ 筆食品業者 |
| 食品違規 | [食藥署食品藥物消費者知識服務網](https://consumer.fda.gov.tw/) | 違規食品查詢 |

### 💼 上市櫃財務資料

| 來源 | 連結 | 說明 |
|---|---|---|
| 公開資訊觀測站 | [mops.twse.com.tw](https://mops.twse.com.tw/) | 上市櫃公司財報、重大訊息 |
| 證交所 OpenAPI | [TWSE OpenAPI](https://openapi.twse.com.tw/) | 上市公司財報 API |
| 櫃買中心 OpenAPI | [TPEx OpenAPI](https://www.tpex.org.tw/web/about_tpex/api/index.php) | 上櫃公司財報 API |

### 📜 專利與商標

| 來源 | 連結 | 說明 |
|---|---|---|
| 智財局 | [經濟部智慧財產局全球商標資訊網](https://twtmsearch.tipo.gov.tw/) | 商標檢索 |
| 智財局 | [專利檢索系統](https://gpss.tipo.gov.tw/) | 專利檢索 |

### 🚧 違規與裁罰紀錄

| 來源 | 連結 | 說明 |
|---|---|---|
| 勞動部違規 | [勞動部勞動條件違反事業單位查詢系統](https://announcement.mol.gov.tw/) | 勞檢違規查詢 |
| 環保署裁罰 | [環境部環保許可資料查詢](https://prtr.moenv.gov.tw/) | 環保裁罰紀錄 |

---

## 📦 本 Repo 提供的資料

| 檔案 | 內容 |
|---|---|
| [`data/industry-codes.csv`](data/industry-codes.csv) | 台灣行業標準分類大類（A-S 字母代碼，中英對照） |
| [`data/taiwan-regions.json`](data/taiwan-regions.json) | 22 個縣市的標準英文 slug 對照（適合做 URL routing） |
| [`data/company-status-codes.md`](data/company-status-codes.md) | 公司營業狀態代碼說明（營業中、解散、歇業等） |

## 🐍 程式範例

[`examples/load_company_csv.py`](examples/load_company_csv.py) — 用 Python pandas 載入 data.gov.tw 的全國公司登記資料 CSV，包含：
- 從 data.gov.tw 下載公開 CSV
- 用 pandas 讀取與基本清理
- 按行業代碼、縣市篩選的範例

```bash
pip install pandas requests
python examples/load_company_csv.py
```

## 📝 授權

- 本 Repo 內容（README、程式範例、CSV 整理）採 [MIT License](LICENSE)
- 所引用的政府開放資料採 [OGDL 1.0](https://data.gov.tw/license)，再利用時請標示來源

## 🤝 貢獻

歡迎 PR 補充新的資料來源或修正錯誤連結。請避免：
- 連結到需要付費才能下載資料的商業 API
- 連結到爬蟲規避工具或反 robots.txt 的服務

## ⚠️ 免責聲明

本 Repo 為**社群維護**的資源整理，**與任何政府機關或商業公司無關**。所有外部連結與工具的著作權、商標權皆屬其原所有人。資料正確性以各原始來源為準。

---

維護者：[NowTo](https://now.to/) ・ Issues 與 PR 歡迎
