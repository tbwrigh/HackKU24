from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine

import os

from handlers import patient_handler, pair_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine(os.getenv("DATABASE_URL"))
    app.state.db = engine
    try:
        yield
    finally:
        engine.dispose()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patient_handler.router)
app.include_router(pair_handler.router)

@app.get("/")
def read_root():
    return {"API Version": "1.1.0"}