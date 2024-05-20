from fastapi import FastAPI
from app.routers import keywords
from app.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Include the routers
app.include_router(keywords.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the KeyBERT Keyword Extraction API"}
