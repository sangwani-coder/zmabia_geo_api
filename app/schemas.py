from pydantic import BaseModel
from dataclasses import dataclass, field
from typing import List, Optional


class CityBase(BaseModel):
    name: str
    population: Optional[int] = None
    province: Optional[str] = None
    is_capital: Optional[bool] = None
    area_km2: Optional[int] = None
    constituencies: List


class ProvinceBase(BaseModel):
    name: str
    capital: str
    population: int
    area_km2: int
    constituencies: int


class ConstituencyBase(BaseModel):
    name: str

class ProvinceWithCities(ProvinceBase):
    cities: List[CityBase]


class ProvinceWithConstituency(ConstituencyBase):
    constituencies: List