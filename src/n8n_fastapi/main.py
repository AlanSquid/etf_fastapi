from fastapi import FastAPI
from n8n_fastapi.api.v1.etf import router as etf_router
from playwright.async_api import async_playwright
import uvicorn

# 定義 lifespan 函數，這是 FastAPI 的一個生命週期事件
# 用來在應用啟動和關閉時執行一些操作
async def lifespan(app: FastAPI):
    # Startup: 啟動 playwright 並存到 app.state 中
    app.state.playwright = await async_playwright().start()
    yield  # 讓 FastAPI 知道啟動中已完成
    # Shutdown: 停止 playwright
    await app.state.playwright.stop()

# 創建 FastAPI 應用
app = FastAPI(lifespan=lifespan)

# 綁定 ETF 路由
app.include_router(etf_router, prefix="/api/v1/etf", tags=["ETF"])

# 添加啟動入口
def main():
    uvicorn.run("n8n_fastapi.main:app", host="0.0.0.0", port=8000, reload=True)
