from mlProject import logger
from mlProject.pipeline.Stage_01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.Stage_02_data_validation import DataValidationPipeline
from omegaconf import DictConfig
import hydra


@hydra.main(version_base=None, config_path='config', config_name="config")
def main(cfg: DictConfig):

    logger.info(f"Data Ingestion Stage started")
    Ingestion_pipeline = DataIngestionPipeline(cfg)
    Ingestion_pipeline.run()
    logger.info(f"Data Ingestion Completed Successfully")

    logger.info(f"Data Validation Stage Started")

    Validation_pipeline = DataValidationPipeline(cfg)

    Validation_pipeline.run()

    logger.info(f"Data Validation Stage Ended")


if __name__ == "__main__":
    main()