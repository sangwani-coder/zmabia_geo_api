from zambia_geo import get_all_provinces, get_province_cities

def list_provinces():
    return get_all_provinces()

def fetch_cities_by_province(province_name: str):
    # Standardize input for validation
    provinces = [p.name.lower() for p in get_all_provinces()]
    if province_name.lower() not in provinces:
        return None
    return get_province_cities(province_name)

def search_cities_globally(query: str):
    results = []
    for province in get_all_provinces():
        cities = get_province_cities(province.name)
        for city in cities:
            if query.lower() in city.name.lower():
                results.append(city)
    return results