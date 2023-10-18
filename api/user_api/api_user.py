from fastapi import APIRouter
from database.user_service import register_user_db, get_user_score_db, show_leaders_score

user_router = APIRouter(prefix='/user', tags=['Users'])


@user_router.post('/register')
async def register_user(name: str, phone_number: str):
    result = register_user_db(name, phone_number)
    return {'status': 1, 'user_id': result}


@user_router.get('/leaders')
async def get_5_leaders():
    result = show_leaders_score()
    return {'status': 1, 'leaders': result}


@user_router.post('/completed')
async def test_finished(user_id: int):
    result = get_user_score_db(user_id)\


    if result:
        return {'status': 1, 'score': result}
    return {'status': 0, 'message': 'User not found'}

