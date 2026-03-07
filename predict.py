import pandas as pd

def predict(n,loaded_model):
    sample_data = pd.DataFrame({"rebound_signal": [n]})
    loaded_preds = loaded_model.predict(sample_data)
    return loaded_preds
