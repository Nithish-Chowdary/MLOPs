from mlProject import logger
from mlProject.pipeline.Stage_01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.Stage_02_data_validation import DataValidationPipeline
from mlProject.pipeline.Stage_03_data_transformation import DataTransformationPipeline
from mlProject.pipeline.Stage_04_model_trainining import ModelTrainingPipeline
from omegaconf import DictConfig
from mlProject.config.configuration import ConfigurationManagaer
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

    logger.info(f"Data Tranfromation Stage had started")
    data_transformation_pipeline = DataTransformationPipeline(cfg)
    data_transformation_pipeline.run()
    logger.info(f"Data Tranformation Stage has Ended")

    logger.info(f"Model Training Stage has Started")

    model_train_pipeline = ModelTrainingPipeline(cfg)

    model_train_pipeline.run()

    logger.info(f"Model Training Stage has Ended")


if __name__ == "__main__":
    main()