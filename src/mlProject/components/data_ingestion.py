from src.mlProject.entity.config_entity import DataIngestionConfig
from pathlib import Path
import os
from urllib.request import urlretrieve
import zipfile
from src.mlProject import logger
from src.mlProject.utils.common import get_size


class DataIngestion:

    def __init__(self, config: DataIngestionConfig):

        self.config = config

    def download_file(self):

        if not os.path.exists(self.config.local_data_file):

            filename, headers = urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )

            logger.info(f"{filename} is downloaded from the url:{self.config.source_URL}")

        logger.info(f"Data File already exists at path:{self.config.local_data_file} and"
                    f" file size is:{get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)

        logger.info(f"The zip file is extracted successfully to path: {self.config.unzip_dir}")







