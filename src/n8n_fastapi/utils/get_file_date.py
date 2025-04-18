import polars as pl

def get_file_date(file_path) -> str:
    try:
        # 用正則表達匹配日期部分
        date_pattern = r"(\d{4}/\d{2}/\d{2})"
        # 讀取檔案的第一行，並用正則表達式提取日期
        file_date = (
            pl.read_csv(
                file_path,
                truncate_ragged_lines=True,
                n_rows=1,
                has_header=False,
            )
            .select(pl.col("column_1").str.extract(date_pattern, 1))
            .item()
            .replace("/", "")
        )
        return file_date
    except Exception as e:
        raise ValueError(f"Failed to parse file date from {file_path}: {e}")
    