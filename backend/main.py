from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import storage
from google.oauth2 import service_account
from sqlalchemy import create_engine

import os
import json

from handlers import patient_handler, pair_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine(os.getenv("DATABASE_URL"))
    app.state.db = engine
    gcp_auth_json = json.loads(os.getenv("GCP_KEY"))
    app.state.gcs_client = storage.Client(credentials=service_account.Credentials.from_service_account_info(gcp_auth_json))
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
    """
    Returns the API version
    """
    return {"API Version": "1.2.0"}