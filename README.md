# Zambia Geo API (zambia_geo_api)

A FastAPI-based REST API that provides structured access to Zambian geographic data, powered by the `zambia_geo` package.

## Features
- **Province Listing**: Get all 10 provinces of Zambia and their capitals.
- **City Retrieval**: Fetch all cities within a specific province.
- **Global Search**: Search for any city across the entire country.
- **Validation**: Automatic validation of province names and search queries.


## Setup Instructions

1. **Clone the repository**

            git clone [https://github.com/yourusername/zambia_geo_api.git](https://github.com/yourusername/zambia_geo_api.git)
            cd zambia_geo_api

2. Create a Virtual Environment
   
            python -m venv venv
            source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

            pip install -r requirements.txt

3. Run the API

            uvicorn app.main:app --reload


## API Endpoints
| Method | Endpoint | Description |
|---------|----------|-------------|
| GET |  /api/v1/provinces | List all provinces and capitals|
| GET |  /api/v1/provinces/{name}/cities | Get cities for a specific province|
| GET | /api/v1/cities/search?q={query} | Search for cities by name|

Interactive Documentation

Once the server is running, visit:

         Swagger UI: http://127.0.0.1:8000/docs

         ReDoc: http://127.0.0.1:8000/redoc