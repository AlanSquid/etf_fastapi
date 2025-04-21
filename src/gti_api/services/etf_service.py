from playwright.async_api import Playwright
import os
from gti_api.utils.get_file_date import get_file_date

async def download_etf_csv(playwright: Playwright, etf_code: str):
    if etf_code not in ["0050", "0056"]:
        raise ValueError("ETF code must be either '0050' or '0056'")

    # 設定下載路徑
    TARGET_DIR = f"/mnt/etf_data/{etf_code}"  # 最終儲存位置

    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = await chromium.launch(headless=True)
    context = await browser.new_context(accept_downloads=True)
    page = await context.new_page()
    try:
        await page.goto(f"https://www.yuantaetfs.com/product/detail/{etf_code}/ratio")

        download_button = page.locator("text=匯出excel")
        # 等待按鈕可點擊
        await download_button.wait_for(state="visible")

        # Start waiting for the download
        async with page.expect_download() as download_info:
            # Perform the action that initiates download
            await download_button.click()
        download = await download_info.value

        # 確保目錄存在
        os.makedirs(TARGET_DIR, exist_ok=True)
        
        # 暫存下載檔案
        tmp_path = os.path.join(TARGET_DIR, "temp_download.csv")
        await download.save_as(tmp_path)
        
        # 取得檔案日期
        file_date = get_file_date(tmp_path)
        
        # 編輯正確檔案名稱
        filename = f"{file_date}_{etf_code}.csv"
        target_path = os.path.join(TARGET_DIR, filename)
        
        # 檢查檔案是否已存在，若存在則加上編號
        counter = 1
        while os.path.exists(target_path):
            filename = f"{file_date}_{etf_code}({counter}).csv"
            target_path = os.path.join(TARGET_DIR, filename)
            counter += 1
        
        # 重新命名檔案
        os.rename(tmp_path, target_path)

    except Exception as e:
        print(f"下載失敗: {e}")
    finally:
        await browser.close()
