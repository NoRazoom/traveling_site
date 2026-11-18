from fastapi import APIRouter

from api.endpoints import places_router, start_router, trip_router


main_router = APIRouter(prefix="/api")

main_router.include_router(
    start_router, prefix='', tags=['getting start']
)
main_router.include_router(
    places_router, prefix='/places', tags=['places']
)
main_router.include_router(
    trip_router, prefix='/trips', tags=['trips']
)
