# 專案啟動與環境設定

## 1. 複製環境變數檔案

將專案中的環境變數範例檔案`.env.example`複製成新的 `.env` 檔案，並根據需求修改各項環境變數

- ETF_DATA_PATH: 下載相關ETF的CSV檔案的存放路徑
- N8N_DATA_PATH: n8n相關的檔案路徑
- FASTAPI_PORT
- N8N_PORT


### 若專案clone下來的位置在wsl環境:

1. 下載檔案想直接存放在WSL環境，路徑範例寫:`/home/<使用者名稱>/.../etf_data`
2. 下載檔案想存放在Win環境，則路徑要寫:`/mnt/c/users/<使用者名稱>/.../etf_data`

### 若專案clone下來的位置在Win環境:

下載檔案的路徑要用反斜線，例如: `C:\Users\<使用者名稱>\Documents\...\etf_data`

## 2. 執行docker compose來啟動服務

指令: `docker compose up -d --build`

## 3. 在N8N中使用HTTP Request節點來向FastAPI伺服器請求

由於N8N跟FastAPI伺服器的container都由docker compose來管理，已經建立了同一個network
因此請求路徑可以寫`fastapi:<port>`

例如:
`http://fastapi:8000/api/v1/etf/download`







