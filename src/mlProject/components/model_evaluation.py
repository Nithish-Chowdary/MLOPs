from mlProject import logger
from omegaconf import DictConfig
from mlProject.entity.config_entity import ModelEvaluationConfig
import pandas as pd
import joblib
import mlflow
import numpy as np
import mlflow.sklearn
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


class ModelEvaluation:

    def __init__(self, config: ModelEvaluationConfig ):

        self.config = config
        self.model = joblib.load(self.config.model_path)


    def eval_metrics(self, actual, pred):

        rmse = np.sqrt(mean_squared_error(actual, pred))

        mae = mean_absolute_error(actual, pred)

        r2 = r2_score(actual, pred)

        return rmse, mae, r2


    def eval(self):

        test_data = pd.read_csv(self.config.test_data_path)

        test_data_inputs = test_data.drop([self.config.target_column], axis=1)
        test_data_outputs = test_data[[self.config.target_column]]

        mlflow.set_tracking_uri(self.config.mlflow_uri)
        mlflow.set_registry_uri(self.config.mlflow_uri)

        with mlflow.start_run(run_name="MLFLOW_WINE_QUALITY"):

            predictions = self.model.predict(test_data_inputs)

            (rmse, mae, r2) = self.eval_metrics(test_data_outputs, predictions)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metrics({
                "RMSE" : rmse,
                "MAE" : mae,
                "R2_Score" : r2
            })

            mlflow.sklearn.log_model(self.model, "model")

            model_uri = f"runs:/{mlflow.active_run().info.run_id}/model"
            model_name = "Wine_Quality_Model_ElasticNet"

            mlflow.register_model(model_uri,model_name,tags={"version": "InitialRUN"})

            logger.info(f"Model {model_name} registered with versioning in MLFLOW.")
            logger.info(f"Metrics - RMSE;{rmse}, MAE:{mae}, R2_Score;{r2}")










