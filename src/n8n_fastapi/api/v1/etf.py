from fastapi import APIRouter, Depends
from n8n_fastapi.services.etf_service import download_etf_csv_service
from n8n_fastapi.dependencies import get_playwright

router = APIRouter()

@router.get("/download")
async def get_etf_csv(playwright=Depends(get_playwright)):
    await download_etf_csv_service(playwright, "0050")
    await download_etf_csv_service(playwright, "0056")
    return {"success": True, "message": "Downloaded successfully."}