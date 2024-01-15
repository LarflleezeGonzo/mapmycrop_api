from pydantic import BaseModel
class HistoricWeatherRequest(BaseModel):
    latitude: float
    longitude: float
    number_of_days: int