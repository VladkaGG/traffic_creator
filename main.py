from fastapi import FastAPI
from models import User


app = FastAPI()


@app.get('/hello')
async def hello_world():
    return {'Hello fast-api world'}


@app.post('/user')
async def create_user(user: User):
    return {"request body": user}


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
