"""
範例：用 pandas 載入 data.gov.tw 的全國公司登記資料 CSV

這個範例展示如何從 data.gov.tw 下載官方公開的公司登記 CSV 資料、
用 pandas 讀取，並按行業/縣市做基本篩選。

完全使用「政府開放資料」(data.gov.tw)，不依賴任何第三方 API。
資料採 OGDL 1.0 授權，可自由使用、改作、商業使用，但須標示來源。

依賴：
    pip install pandas requests

執行：
    python examples/load_company_csv.py
"""

from pathlib import Path
import sys

try:
    import pandas as pd
    import requests
except ImportError:
    print("請先安裝依賴：pip install pandas requests")
    sys.exit(1)


# data.gov.tw 全國公司登記基本資料的下載頁面：
#   https://data.gov.tw/dataset/9101
# 該頁面提供 CSV 下載連結（連結會偶爾更新，請以官方頁面為準）。
DATASET_PAGE = "https://data.gov.tw/dataset/9101"

# 範例 CSV 路徑（請從上方頁面取得當前的下載 URL 後填入此處）
SAMPLE_CSV_URL = ""  # 例如：https://data.gov.tw/api/v2/rest/dataset/.../resource/...


def download_csv(url: str, dest: Path) -> None:
    """從給定 URL 下載 CSV 到本地檔案"""
    print(f"下載中: {url}")
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    dest.write_bytes(resp.content)
    print(f"已儲存到: {dest} ({dest.stat().st_size:,} bytes)")


def load_companies(csv_path: Path) -> pd.DataFrame:
    """讀取公司登記 CSV，做基本欄位清理"""
    # data.gov.tw 的 CSV 通常是 UTF-8，但偶爾會是 BIG5
    try:
        df = pd.read_csv(csv_path, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(csv_path, encoding="big5")

    print(f"讀取完成: {len(df):,} 筆公司")
    print(f"欄位: {list(df.columns)}")
    return df


def filter_by_industry(df: pd.DataFrame, industry_letter: str) -> pd.DataFrame:
    """按行業大類字母（A-S）篩選"""
    # 實際欄位名請依 CSV 內容調整，這裡假設叫「行業代號」
    col = next((c for c in df.columns if "行業" in c), None)
    if not col:
        print("找不到行業欄位，請檢查 CSV 結構")
        return df
    return df[df[col].astype(str).str.startswith(industry_letter)]


def filter_by_city(df: pd.DataFrame, city_name: str) -> pd.DataFrame:
    """按縣市名稱篩選（例如「臺北市」「高雄市」）"""
    col = next((c for c in df.columns if "地址" in c or "縣市" in c), None)
    if not col:
        print("找不到地址/縣市欄位")
        return df
    return df[df[col].astype(str).str.contains(city_name, na=False)]


def main() -> None:
    if not SAMPLE_CSV_URL:
        print(f"請先到 {DATASET_PAGE} 取得最新的 CSV 下載 URL，")
        print("並填入此檔案頂部的 SAMPLE_CSV_URL 變數後再執行。")
        return

    cache_dir = Path("./cache")
    cache_dir.mkdir(exist_ok=True)
    csv_path = cache_dir / "companies.csv"

    if not csv_path.exists():
        download_csv(SAMPLE_CSV_URL, csv_path)

    df = load_companies(csv_path)

    # 範例 1：篩選「製造業」（行業代號 C 開頭）
    manufacturing = filter_by_industry(df, "C")
    print(f"\n製造業公司數：{len(manufacturing):,}")

    # 範例 2：篩選「臺北市」的公司
    taipei = filter_by_city(df, "臺北市")
    print(f"臺北市公司數：{len(taipei):,}")

    # 範例 3：交集 — 臺北市的製造業公司
    taipei_manufacturing = filter_by_city(manufacturing, "臺北市")
    print(f"臺北市製造業公司數：{len(taipei_manufacturing):,}")


if __name__ == "__main__":
    main()
