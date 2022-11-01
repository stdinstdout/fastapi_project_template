from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi import FastAPI

from functools import lru_cache


from .database import SessionLocal, engine
from . import config, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@lru_cache()
def get_settings():
    return config.Settings()  # type: ignore


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


