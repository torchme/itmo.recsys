from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/reco/{model_name}/{user_id}")
def reco(model_name: str, user_id: str):
    return {"items": [random.randint(1, 100) for _ in range(10)]}
