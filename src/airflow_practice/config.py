import logging
from pathlib import Path

from pydantic import ConfigDict, Field
from pydantic_settings import BaseSettings

DIR_PATH = Path(__file__).resolve().parent.parent

# Path to the data lake
DATA_PATH = DIR_PATH.parent / "data"


class Config(BaseSettings):
    dir_path: Path = Field(
        default=DIR_PATH,
        description="The directory path for the application. (src/...)",
    )

    data_path: Path = Field(
        default=DATA_PATH,
        description="The path guiding to the data lake.",
    )

    data_source_prefix: str = Field(
        default="https://www.ncei.noaa.gov/pub/data/uscrn/products/subhourly01",
        description="Data source",
    )

    model_config = ConfigDict(protected_namespaces=("settings_",))


def setup_logging() -> None:
    """Configure the root logger."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler()],  # Directs logs to stdout, visible in CloudWatch
        force=True,
    )


settings = Config()
