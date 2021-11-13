from typing import Union
import requests
import json
from pydantic import fields
from pydantic.dataclasses import dataclass

"""https://alerts.weather.gov/cap/oh.php?x=2

    [extended_summary]
"""


@dataclass
class ZoneProperties:
    id: str
    type: str
    name: str
    effectiveDate: str
    expirationDate: str
    state: str
    cwa: list[str]
    forecastOffices: list[str]
    timeZone: list[str]
    observationStations: list[str]
    radarStation: Union[str, None]


# load zone info objects from json file
with open("weather_example.json", "r") as data:
    out = [ZoneInfo(**i) for i in json.load(data).features][0]


# load zone info objects from json file
with open("zone_schema.exmple.json", "r") as data:
    json_data = json.load(data)
out = [ZoneProperties(**i) for i in json_data["features"][0]["properties"]]
