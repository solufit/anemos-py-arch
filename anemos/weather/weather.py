from .schemas import AnemosWeather
from typing_extensions import deprecated

@deprecated("この関数はv1以降で正式に実装される予定です。")
def get(postcode: str, start_date: str, end_date: str, object_type: str | None = None) -> list[AnemosWeather]:
    return []

@deprecated("この関数はv1以降で正式に実装される予定です。")
def get_weekly(postcode: str) -> list[AnemosWeather]:
    return []

@deprecated("この関数はv1以降で正式に実装される予定です。")
def get_daily(postcode: str) -> list[AnemosWeather]:
    return []
