from fastapi import APIRouter, Request
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.pair import Pair

router = APIRouter(prefix="/pair", tags=["content"])

@router.get("/")
async def get_pairs(request: Request):
    with Session(request.app.state.db) as session:
        return session.execute(select(Pair)).scalars().all()

@router.get("/{patient_id}")
async def get_pairs_by_patient_id(req: Request, patient_id: int):
    with Session(req.app.state.db) as session:
        return session.execute(select(Pair).filter(Pair.patient_id == patient_id)).scalars().all()

