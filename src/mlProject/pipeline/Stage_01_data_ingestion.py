from omegaconf import DictConfig
from src.mlProject.components.data_ingestion import DataIngestion
from src.mlProject.config.configuration import ConfigurationManagaer
from src.mlProject import logger
import hydra




class DataIngestionPipeline:

    def __init__(self, cfg: DictConfig):

        self.config_manager = ConfigurationManagaer(cfg)

    def run(self):

        dataingestion_config = self.config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(dataingestion_config)

        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

@hydra.main(version_base=None, config_path='config', config_name="config")
def main(cfg: DictConfig):

    logger.info(f"Data Ingestion Stage started")
    pipeline = DataIngestionPipeline(cfg)
    pipeline.run()

    logger.info(f"Data Ingestion Completed Successfully")

if __name__ =="__main__":
    main()


