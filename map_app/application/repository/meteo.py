from typing import List
import httpx
from fastapi import HTTPException

async def call_meteo_api(
    latitude: float, longitude: float, number_of_days: int
) -> List[dict]:
    api_url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&past_days={number_of_days}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)

        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail="Failed to fetch data from the third-party API",
            )
