from .schemas import AnemosWeather

def get(postcode: str, start_date: str, end_date: str, object_type: str | None = None) -> list[AnemosWeather]:
    return []

def get_weekly(postcode: str) -> list[AnemosWeather]:
    return []

def get_daily(postcode: str) -> list[AnemosWeather]:
    return []
