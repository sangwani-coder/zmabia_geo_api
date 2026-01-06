from fastapi import APIRouter, HTTPException, Query
from typing import List
from app import services, schemas

router = APIRouter()


@router.get("/provinces", response_model=List[schemas.ProvinceBase])
def get_provinces():
    return services.list_provinces()


@router.get(
    "/provinces/{province_name}/cities", response_model=List[schemas.CityBase])
def get_province_cities(province_name: str):
    cities = services.fetch_cities_by_province(province_name)
    if cities is None:
        raise HTTPException(status_code=404, detail="Province not found")
    return cities


@router.get("/cities/search", response_model=List[schemas.CityBase])
def search_cities(q: str = Query(..., min_length=2)):
    return services.search_cities_globally(q)
