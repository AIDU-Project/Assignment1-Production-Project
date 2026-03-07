from fastapi import FastAPI
import load_model 
import predict
app = FastAPI()
model_path = "models/rf_rebound_density.joblib"
model = load_model.load(model_path)


riel_pass = "matkhaumanhvl"
@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}


@app.get("/predict/{signal}")
def predictAPI(signal):
    result = predict.predict(signal,model)
    print(type(result))
    return result[0]

@app.get("/lololo/{signal}")
def lolololo(signal):
    return 'lololo'

@app.get("/login/{password}")

def checking(password):
    if password == riel_pass:
        return {"status" : "success","path":model_path}
    else:
        return {"status" : "invalid"}
