from fastapi import APIRouter

from application.api import map_api

api_router = APIRouter()
api_router.include_router(map_api.router, tags=["Map API"])

