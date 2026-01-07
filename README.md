# Zambia Geo API (zambia_geo_api)
A FastAPI-based REST API that provides structured access to Zambian geographic data, powered by the [zambia_geo](https://github.com/sangwani-coder/zambia_geo/) package.


## Features

Features & Endpoints
- Visual Landing Page: A clean UI to explain the API to non-technical users.
- Provinces: List all 10 provinces.
- City Search: Fuzzy search across the entire country.
- Documentation: Auto-generated Swagger and ReDoc.

## 🤝 Contributing

We love contributors! Please see our CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## Project Structure

### 📜 Maintainers

Maintained by the _Zambian Developer Community_.

- Lead Contributor: Sangwani Zyambo [github](https://github.com/sangwani-coder/:

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
| GET |  /api/v1/provinces/{name}/cities | Get towns for a specific province|
| GET | /api/v1/cities/search?q={query} | Search for cities by name|
| GET | /api/v1/provinces/{province_name}/constituencies/ | Get constituencies for specific town|

Interactive Documentation

Once the server is running, visit:

         Swagger UI: http://127.0.0.1:8000/docs

         ReDoc: http://127.0.0.1:8000/redoc

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
