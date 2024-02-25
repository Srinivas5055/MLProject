import os 
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.expection import CustomException
from src.logger import logging
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts',"train.csv")
    test_data_path = os.path.join('artifacts',"test.csv")
    raw_data_path = os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestionConfig = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered in to data ingestion method')
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('dataset read as dataframe')
            os.makedirs(os.path.dirname(self.ingestionConfig.train_data_path),exist_ok=True)
            df.to_csv(self.ingestionConfig.raw_data_path,index=False,header=True)
            logging.info('Train test Split Intiated')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestionConfig.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestionConfig.test_data_path,index=False,header=True)
            logging.info('Ingestion of the data is completed')
            return (
                 self.ingestionConfig.train_data_path,
                 self.ingestionConfig.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()
    # logging.info(train_data)
    # logging.info(test_data)
    data_transformation = DataTransformation()
    # data_transformation.initiate_data_transformation
    data_transformation.initiate_data_transformation(train_data,test_data)
    # data_transformation.initiate_data_transformation(train_data,test_data)





