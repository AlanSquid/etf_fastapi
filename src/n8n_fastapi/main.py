from fastapi import FastAPI
from n8n_fastapi.routes.etf_routes import router as etf_router

# 創建 FastAPI 應用
app = FastAPI()

# 綁定 ETF 路由
app.include_router(etf_router, prefix="/api/etf", tags=["ETF"])
