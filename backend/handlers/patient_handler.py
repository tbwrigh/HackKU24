from fastapi import APIRouter, Request, Body
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.patient import Patient

router = APIRouter(prefix="/patient", tags=["patient"])

@router.get("/")
async def get_patients(req: Request):
    """
    Get all patients
    """
    with Session(req.app.state.db) as session:
        return session.execute(select(Patient)).scalars().all()

@router.get("/{patient_id}")
async def get_patient_by_id(req: Request, patient_id: int):
    """
    Get a patient by ID
    """
    with Session(req.app.state.db) as session:
        return session.execute(select(Patient).filter(Patient.id == patient_id)).scalars().first()

@router.post("/")
async def create_patient(req: Request, name: str = Body(...), id_string: str = Body(...)):
    """
    Create a patient
    """
    req.app.state.gcs_client.create_bucket(id_string)
    with Session(req.app.state.db) as session:
        patient = Patient(name=name, id_string=id_string)
        session.add(patient)
        session.commit()
        return patient

@router.delete("/{patient_id}")
async def delete_patient(req: Request, patient_id: int):
    """
    Delete a patient by ID
    """
    with Session(req.app.state.db) as session:
        patient = session.execute(select(Patient).filter(Patient.id == patient_id)).scalars().first()
        req.app.state.gcs_client.get_bucket(patient.id_string).delete()
        session.delete(patient)
        session.commit()
        return patient