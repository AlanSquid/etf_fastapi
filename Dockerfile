FROM python:3.12-slim-bookworm

# 安裝uv和其他必要套件
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        git \
        build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 將 uv 的 binary 加到 PATH（uv 安裝 script 已自動加進 /root/.cargo/bin）
ENV PATH="/root/.cargo/bin:$PATH"

# 建立工作目錄
WORKDIR /app

# 複製專案檔案（根目錄含 pyproject.toml）
COPY . .

# 安裝 Python 套件
RUN uv sync
RUN uv run playwright install
RUN uv run playwright install-deps

# 設定啟動命令
CMD ["uv", "run", "start"]