from fastapi import APIRouter
from n8n_fastapi.controllers.etf_controller import download_etf_csv

router = APIRouter()

@router.get("/download")
async def get_etf_csv():
    return await download_etf_csv()