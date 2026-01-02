from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import candidate
from app.routers import candidates

app = FastAPI(title="Manpower Platform API")

Base.metadata.create_all(bind=engine)

app.include_router(candidates.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
