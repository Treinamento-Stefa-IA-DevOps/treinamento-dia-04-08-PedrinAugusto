import pickle
from fastapi import FastAPI

app = FastAPI()
@app.post('/model')

## Coloque seu codigo na função abaixo

def titanic(Sex: int, Age: float, Lifeboat: int, Pclass: int):
    
    with open('model/Titanic.pkl', 'rb') as fid:
        titanic = pickle.load(fid)
    
    data = [Sex, Age, Lifeboat, Pclass]
    result = titanic.predict(data)



@app.get('/model')
    
def get():
    return {"survived": "bool", "status": "int", "message": "string"}
