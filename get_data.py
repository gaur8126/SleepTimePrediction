import pymongo
import pandas as pd
import numpy as np 
import os 
import sys 
import certifi
from dotenv import load_dotenv
import json

from src.logger.logger import logging
from src.exception.exception import CustomException

ca = certifi.where()

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


class SleepDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
        
    def convert_csv_to_json(self,filepath):
        try:
            logging.info("converting csv into json form ")
            data = pd.read_csv(filepath)
            data.reset_index(drop = True ,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records 
        except Exception as e:
            raise CustomException(e,sys)
        
    def push_data_to_mongodb(self,records,database,collection):
        try:
            logging.info("pushing data into mongodb")

            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)

            return len(self.records)
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    FILE_PATH = "sleeptimedata/sleeptime_prediction_dataset.csv"
    database = "SleepTime"
    collection = "sleeptimedata"
    obj = SleepDataExtract()
    records = obj.convert_csv_to_json(FILE_PATH)
    obj.push_data_to_mongodb(records,database,collection)