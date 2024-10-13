from omegaconf import DictConfig, OmegaConf
import hydra
from src.mlProject.config.configuration import ConfigurationManagaer
from src.mlProject.components.data_validation import  DataValidation
from mlProject import logger



class DataValidationPipeline:

    def __init__(self, cfg: DictConfig):

        self.config = ConfigurationManagaer(cfg)

    def run(self):

        data_validation_config = self.config.get_data_validation_config()

        data_validation = DataValidation(data_validation_config)

        data_validation.validate_all_columns()

@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg: DictConfig):

    logger.info(f"Data Validation Stage Started")

    pipeline = DataValidationPipeline(cfg)

    pipeline.run()

    logger.infor(f"Data Validation Stage Ended")


if __name__ == "__main__":
    main()


