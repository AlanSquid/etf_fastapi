from n8n_fastapi.services.etf_service import download_etf_csv_service
from playwright.async_api import async_playwright

async def download_etf_csv():
    async with async_playwright() as playwright:
        await download_etf_csv_service(playwright, "0050")
        await download_etf_csv_service(playwright, "0056")
        await playwright.stop()
        return {"download": "success"}