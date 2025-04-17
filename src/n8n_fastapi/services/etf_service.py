from playwright.async_api import Playwright
import os
from datetime import datetime


async def download_etf_csv_service(playwright: Playwright, etf_code: str):
    if etf_code not in ["0050", "0056"]:
        raise ValueError("ETF code must be either '0050' or '0056'")

    # 設定下載路徑
    TARGET_DIR = f"/mnt/c/users/squid/documents/etf/{etf_code}"  # 最終儲存位置

    today = datetime.today().strftime("%Y%m%d")
    filename = f"{today}_{etf_code}.csv"

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

        # Wait for the download process to complete and save the downloaded file somewhere
        await download.save_as(os.path.join(TARGET_DIR, filename))
    except Exception as e:
        print(f"下載失敗: {e}")
    finally:
        await browser.close()
