import os
import urllib.request as request
import zipfile
from src.textSummarizer.logging import logger
from src.textSummarizer.utils.common import get_size
from src.textSummarizer.entity import DataIngestionConfig


class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )

            logger.info(f"{filename} dowloaded with following info: \n{header}")
        else:
            logger.info(f"file are already existed")

    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as f:
            f.extractall(unzip_path)

            
