import os
import urllib.request as request
from zipfile import ZipFile
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier import logger
from cnnClassifier.utils import get_size
from tqdm import tqdm
from pathlib import Path

class DataIngestion:
    
    def __init__(self, config : DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Download started...")
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  
    
    
    
    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith("jpg") and ("Cat" in f or "Dog" in f)]
    
    def _preprocess(self, zf: ZipFile, f:str, working_dir:str):
        target_file_path = os.path.join(working_dir,f)
        if not os.path.exists(target_file_path):
            zf.extract(f,working_dir)
            
        if os.path.getsize(target_file_path == 0):
            logger.info("Removinf files wihich have 0 size")
            os.remove(target_file_path)

    def unzip_and_clean(self):
        logger.info("Unzipping the file and removing unwanted files...")
        with ZipFile(file=self.config.local_data_file, mode='r') as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)         