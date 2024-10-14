from src.mlProject.config.configuration import DataTransformationConfig
from src.mlProject.components.data_transformation import DataTransformation
from omegaconf import DictConfig
from src.mlProject.config.configuration import  ConfigurationManagaer
import hydra
from mlProject import logger


class DataTransformationPipeline:

    def __init__(self, cfg: DictConfig):

        self.config = ConfigurationManagaer(cfg)

    def run(self):

        data_transformation_config = self.config.get_data_transformation_config()

        data_transformation = DataTransformation(data_transformation_config)

        data_transformation.train_test_split()


@hydra.main(version_base=None, config_name="config", config_path="config")
def main(cfg: DictConfig):

    logger.info(f"Data Tranfromation Stage had started")
    data_transformation_pipeline = DataTransformationPipeline(cfg)
    data_transformation_pipeline.run()
    logger.info(f"Data Tranformation Stage has Ended")

if __name__ == "__main__":
    main()



