from fastapi import APIRouter, Request, Body
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.patient import Patient

router = APIRouter(prefix="/patient", tags=["patient"])

@router.get("/")
async def get_patients(req: Request):
    with Session(req.app.state.db) as session:
        return session.execute(select(Patient)).scalars().all()

@router.get("/{patient_id}")
async def get_patient_by_id(req: Request, patient_id: int):
    with Session(req.app.state.db) as session:
        return session.execute(select(Patient).filter(Patient.id == patient_id)).scalars().first()

@router.post("/")
async def create_patient(req: Request, name: str = Body(...), id_string: str = Body(...)):
    with Session(req.app.state.db) as session:
        patient = Patient(name=name, id_string=id_string)
        session.add(patient)
        session.commit()
        return patient

@router.put("/{patient_id}")
async def update_patient(req: Request, patient_id: int, name: str = Body(...), id_string: str = Body(...)):
    with Session(req.app.state.db) as session:
        patient = session.execute(select(Patient).filter(Patient.id == patient_id)).scalars().first()
        patient.name = name
        patient.id_string = id_string
        session.commit()
        return patient

@router.delete("/{patient_id}")
async def delete_patient(req: Request, patient_id: int):
    with Session(req.app.state.db) as session:
        patient = session.execute(select(Patient).filter(Patient.id == patient_id)).scalars().first()
        session.delete(patient)
        session.commit()
        return patient