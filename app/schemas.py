from pydantic import BaseModel
from typing import List, Optional


class CityBase(BaseModel):
    name: str
    population: Optional[int] = None
    province: Optional[str] = None
    is_capital: Optional[bool] = None
    area_km2: Optional[int] = None


class ProvinceBase(BaseModel):
    name: str
    capital: str
    population: int
    area_km2: int


class ProvinceWithCities(ProvinceBase):
    cities: List[CityBase]
