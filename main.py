from fastapi import FastAPI
from fastapi.responses import Response
from models import User
from mongoworker import Model

URI = 'mongodb://127.0.0.1:27017/data'
model = Model(URI)
app = FastAPI()


@app.get('/hello')
async def hello_world():
    return {'Hello fast-api world'}


@app.post('/user')
async def create_user(user: User):
    model.collection = 'user'
    result = await model.insert_one(user.dict(by_alias=True))
    return {'inserted_id': result}


@app.get('/user')
async def get_user_validation(password: str):
    return {"query parameter": password}


@app.get('/user/{id}')
async def get_user_by_id(id: str):
    return {"query id": id}


@app.get('/user/{id}/tasks')
async def get_user_by_task(id: str, status: str, order: str = 'asc'):
    return {
        "pet id": id,
        "query status": status,
        "query order": order
    }
