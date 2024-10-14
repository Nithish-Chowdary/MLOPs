from mlProject import logger
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.config.configuration import ConfigurationManagaer
import hydra
from omegaconf import DictConfig

class ModelEvaluationPipeline:

    def __init__(self, cfg: DictConfig):

        self.config = ConfigurationManagaer(cfg)

    def run(self):

        model_eval_config = self.config.get_model_evaluation_config()

        model_eval = ModelEvaluation(model_eval_config)

        model_eval.eval()


@hydra.main(version_base=None, config_name="config", config_path="config")
def main(cfg):

    logger.info(f"Trained Model is being laoded to perform Evaluation on Test Data")

    EvaluationPipeline = ModelEvaluationPipeline(cfg)

    EvaluationPipeline.run()

    logger.info(f" Model Evaluation is succesfully completed.")


