import os
import sys
import dill
from src.exception import CustomException
from src.logger import logging

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
import numpy as np
import pandas as pd

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as obj_file:
            dill.dump(obj,obj_file)
    except Exception as e:
        raise CustomException(str(e))
def evaluate_model(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}
        fitted_models={}

        for model_name, model in models.items():
            para = param.get(model_name, {})
            gs = GridSearchCV(model, para, cv=3, n_jobs=-1, scoring='r2')
            gs.fit(X_train, y_train)

            best_model = gs.best_estimator_

            fitted_models[model_name] = best_model

            pred_test = best_model.predict(X_test)
            test_model_score = r2_score(y_test, pred_test)

            report[model_name] = test_model_score


        return report,fitted_models

    except Exception as e:
        raise CustomException(str(e),sys)

def load_object(file_path):
    try:
        with open(file_path,"rb") as obj_file:
            return dill.load(obj_file)
    except Exception as e:
        raise CustomException(str(e),sys)