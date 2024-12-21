from pathlib import Path

import logging

import requests
from airflow_practice.config import settings

logger = logging.getLogger(__name__)


def download_file(filename: str, yr: str | int = 2020, data_dir: str | Path = "./") -> None:
    """Function to download the source data into the data lake.

    Args:
        filename (str): _description_
        yr (str | int, optional): _description_. Defaults to 2020.
        data_dir (str | Path, optional): _description_. Defaults to "./".
    """
    # Get the data from the data source
    r = requests.get(
        f"{settings.data_source_prefix}/{yr}/{filename}",
        timeout=10,
    )
    r.raise_for_status()

    # Path to store the data (Data lake)
    path = Path(data_dir) if not isinstance(data_dir, Path) else data_dir

    # Check the existence of the specified path
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        logger.info("Create %s", path)

    # Download the data into the data lake
    with (path / filename).open("wb") as f:
        f.write(r.content)

    logger.info("Saved %s", path / filename)
