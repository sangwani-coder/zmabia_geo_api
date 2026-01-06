from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import router

app = FastAPI(
    title="Zambia Geo API", description="API for Zambian Geographic Data")

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")


# Serve the index.html at the root
@app.get("/", include_in_schema=False)
async def serve_home():
    """Endpoint serves the static landing page for non technial users"""
    return FileResponse("static/index.html")


app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
