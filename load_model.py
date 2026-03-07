import joblib
import pandas as pd
import os

def load(model_path):
    loaded_model = joblib.load(model_path)
    print(f"Model loaded from: {model_path}")
    return loaded_model
    

