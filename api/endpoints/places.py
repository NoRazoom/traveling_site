from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_places():
    return {'А это': 'будущая страница с выбранными местами'}

@router.get('/{place_id}')
async def get_place(place_id):
    return {'Место под интексом': place_id}