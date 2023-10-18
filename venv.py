from fastapi import FastAPI, Body
from api.test_process_api.process_api import test_process_router
from api.user_api.api_user import user_router
from database import Base, engine

Base.metadata.create_all(bind=engine)a



app = FastAPI(docs_url='/')


app.include_router(user_router)
app.include_router(test_process_router)

@app.get('/hello')
async def hello():
    return {'message': 'Hello World'}


@app.get('/param-example')
async def param_example(user_id: int, user_answer: str):
    return {'message': f'{user_id} has 10 answers {user_answer}'}


@app.post('/hello')
async def first_post(name: str, phone_number: int):
    return {name: phone_number}


@app.put('/test-body')
async def   test_body(header: str = Body(...), main_text: str = Body(default='Text Example')):
    return {'body_params': [header, main_text]}




# in terminal
# uvicorn venv:app --reload

