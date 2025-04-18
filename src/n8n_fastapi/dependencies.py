from fastapi import Request

# 定義一個獲取 playwright 的依賴函數
def get_playwright(request: Request):   
    return request.app.state.playwright