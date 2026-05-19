from fastapi import FastAPI

from app.core.config import settings

from app.api.routes import leads

app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(
    leads.router,
    prefix="/leads",
    tags=["Leads"]
)

@app.get("/")
async def root():
    return {
        "message": "Legion AI Sales Running"
    }