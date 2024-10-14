from src.mlProject.entity.config_entity import DataTransformationConfig
import os
import pandas as pd
from src.mlProject import logger
from sklearn.model_selection import train_test_split



class DataTransformation:

    def __init__(self, config: DataTransformationConfig):

        self.config = config

    def train_test_split(self):

        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data, train_size=0.8)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logger.info(f"Data has been splitted into Train and Test sets")
        logger.info(train.shape)
        logger.info(test.shape)












