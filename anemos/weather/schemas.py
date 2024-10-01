from pydantic import BaseModel

class AnemosWeather(BaseModel):
    object_type: str
    areacode: str
    title: str
    status: str
    detail: str
    reported_at: str
    info_domain: str
    info_object_id: str