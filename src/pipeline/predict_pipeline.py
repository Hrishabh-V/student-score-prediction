import sys,os
import pandas as pd
from src.exception.exception import CustomException
from src.util.util import load_object
from src.util.logger import logging

logger=logging.getLogger(__name__)
class PredictPipeline:
    ''' Pipeline to predict '''
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path = os.path.join("notebook", "artifacts", "ridge_regression.pkl")
            preprocessor_path=os.path.join('notebook','artifacts','preprocessor.pkl')
            logger.debug("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            logger.debug("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            logger.error(f"error during predicting data {e}")
            raise CustomException(e,sys)





class CustomData:
    '''format for input'''
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):

        ''' Convert incoming data as a dataframe  '''
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            logger.error(f"error during transforming data {e}")
            raise CustomException(e, sys)

