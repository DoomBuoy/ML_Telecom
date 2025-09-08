from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from ml_telecom.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    import subprocess
    import sys
    from pathlib import Path

    # Ensure the raw data directory exists
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
   
    import gdown
    # Download customer_address.csv
    address_url = "https://drive.google.com/uc?id=1IXHnuqOT7cBK5YVCkWE-7ZldZXP2Uk4z"
    address_path = RAW_DATA_DIR / "customer_address.csv"
    logger.info(f"Downloading customer_address.csv to {address_path} ...")
    gdown.download(address_url, str(address_path), quiet=False)
    logger.success(f"Downloaded customer_address.csv to {address_path}")

    # Download customer_satisfaction.csv
    satisfaction_url = "https://drive.google.com/uc?id=1BWMGFf_Y6Hfkwp7FyrK2eaKs5GRTOJV5"
    satisfaction_path = RAW_DATA_DIR / "customer_satisfaction.csv"
    logger.info(f"Downloading customer_satisfaction.csv to {satisfaction_path} ...")
    gdown.download(satisfaction_url, str(satisfaction_path), quiet=False)
    logger.success(f"Downloaded customer_satisfaction.csv to {satisfaction_path}")


if __name__ == "__main__":
    app()
