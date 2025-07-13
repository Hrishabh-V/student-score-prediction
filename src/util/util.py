from src.exception.exception import CustomException
from src.util.logger import logging
import os
import sys
import pickle

logger=logging.getLogger(__name__)

def load_object(file_path):
    ''' Function to load objects'''
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logger.error(f"error during loading  {e}")
        raise CustomException(e, sys)
