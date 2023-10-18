from fastapi import APIRouter
from database.test_service import add_question_db, show_question
from database.user_service import add_user_answer_db


test_process_router = APIRouter(prefix='/test', tags=['Test process'])


@test_process_router.get('/get-questions')
async def get_questions():
    result = show_question()
    if result:
        return {'status': 1, 'questions': result}
    return {'status': 0, 'questions': 'Questions not found in database'}


@test_process_router.post('/check-answer')
async def check_answer(user_id: int, user_answer: int, question_id: int, correctness: bool):
    result = add_user_answer_db(user_id, question_id, user_answer, correctness)

    return {'status': 1 if result else 0}


@test_process_router.post('/add-question')
async def add_question(q_text: str, answer: int, v1: str, v2: str, v3: str = None, v4: str = None):
    result = add_question_db(q_text, answer, v1, v2, v3, v4)

    return {'status': 1, 'message': result}

