""" 
Anemos Weather Schemas
"""
from enum import StrEnum  # noqa: E0611

from pydantic import BaseModel


class AnemosObjectTypes(StrEnum):
    WeatherWarning = "Anemos.WeatherWarning"
    WeatherForecast = "Anemos.WeatherForecast"
    Earthquake = "Anemos.Earthquake"

class AnemosWeather(BaseModel):
    object_type: str
    areacode: str
    title: str
    status: str
    detail: str
    reported_at: str
    info_domain: str
    info_object_id: str
