from application.core.security import validate_token
from fastapi import APIRouter, Depends
from application.repository.meteo import call_meteo_api
from application.schemas import HistoricWeatherRequest

router = APIRouter()


@router.get("/ping", response_model=dict)
async def ping():
    return {"message": "Service is up!"}


@router.get(
    "/historic-weather", dependencies=[Depends(validate_token)], response_model=dict
)
async def historic_weather_endpoint(request: HistoricWeatherRequest = Depends()):
    data = await call_meteo_api(
        latitude=request.latitude,
        longitude=request.longitude,
        number_of_days=request.number_of_days,
    )
    return {"data": data}
