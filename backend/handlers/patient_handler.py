from fastapi import APIRouter, Request
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.patient import Patient

router = APIRouter(prefix="/patient", tags=["patient"])

@router.get("/")
async def get_patients(req: Request):
    with Session(req.app.state.db) as session:
        return session.execute(select(Patient)).scalars().all()

