from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_start():
    return {'Привет!': 'Это будущая начальная страница проекта путешествий'}