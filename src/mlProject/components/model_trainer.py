from src.mlProject.entity.config_entity import ModelTrainerConfig
import pandas as pd
import joblib
from sklearn.linear_model import ElasticNet
from mlProject import logger
import os



class ModelTrainer:

    def __init__(self, config: ModelTrainerConfig):

        self.config = config

    def train(self):

        logger.info(f"Train and Test Data split into Inputs and Outputs Respectively")
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_data_inputs = train_data.drop([self.config.target_column], axis=1)
        train_data_outputs = train_data[[self.config.target_column]]
        test_data_inputs = test_data.drop([self.config.target_column], axis = 1)
        test_data_outputs = test_data[[self.config.target_column]]

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)

        logger.info(f"ElasticNet Model is being fitted onto Train Dataset")
        lr.fit(train_data_inputs, train_data_outputs)


        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
        logger.info(f"Model has been successfully fitted and dumped at:{os.path.join(self.config.root_dir, self.config.model_name)}")










