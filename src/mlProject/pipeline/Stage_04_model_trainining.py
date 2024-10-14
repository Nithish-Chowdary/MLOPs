from omegaconf import DictConfig
import hydra
from mlProject.config.configuration import ConfigurationManagaer
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger




class ModelTrainingPipeline:

    def __init__(self, cfg:DictConfig):

        self.config = ConfigurationManagaer(cfg)

    def run(self):

        model_config = self.config.get_model_trainer_config()

        model_trainer = ModelTrainer(model_config)

        model_trainer.train()

@hydra.main(version_base=None, config_path="config", config_name="config")
def main(cfg:DictConfig):

    logger.info(f"Model Training Stage has Started")

    model_train_pipeline = ModelTrainingPipeline(cfg)

    model_train_pipeline.run()

    logger.info(f"Model Training Stage has Ended")

if __name__ =="__main__":
    main()

