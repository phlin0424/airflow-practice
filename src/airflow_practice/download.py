import logging
from pathlib import Path

import requests

from airflow_practice.config import settings

logger = logging.getLogger(__name__)


def download_file(filename: Path) -> None:
    """Function to download the source data into the data lake.

    Args:
        filename (_type_): _description_
    """
    # Get the data from the data source
    r = requests.get(
        f"{settings.data_source_prefix}/2020/{filename}",
        timeout=10,
    )
    r.raise_for_status()

    # Path to store the data (Data lake)
    path = settings.data_path / ".raw"

    # Download the data into the data lake
    with (path / filename).open("wb") as f:
        f.write(r.content)

    logger.info("Saved %s", path / filename)
