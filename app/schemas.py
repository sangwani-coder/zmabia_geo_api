from pydantic import BaseModel
from typing import List, Optional

class CityBase(BaseModel):
    name: str
    population: Optional[int] = None

class ProvinceBase(BaseModel):
    name: str
    capital: str

class ProvinceWithCities(ProvinceBase):
    cities: List[CityBase]