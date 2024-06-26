from typing import List

from fastapi import APIRouter, Body, Request, status
from fastapi.responses import JSONResponse, StreamingResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

import io

from models.error import ErrorMessage
from models.patient import Patient, PatientResponse

router = APIRouter(prefix="/patient", tags=["patient"])


@router.get("/")
async def get_patients(req: Request) -> List[PatientResponse]:
    """
    Get all patients
    """
    with Session(req.app.state.db) as session:
        return session.execute(select(Patient)).scalars().all()


@router.get(
    "/{patient_id}",
    responses={404: {"description": "Patient not found", "model": ErrorMessage}},
)
async def get_patient_by_id(req: Request, patient_id: int) -> PatientResponse:
    """
    Get a patient by ID
    """
    with Session(req.app.state.db) as session:
        patient = (
            session.execute(select(Patient).filter(Patient.id == patient_id))
            .scalars()
            .first()
        )

        if not patient:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": "Patient not found"},
            )

        return patient


@router.post(
    "/",
    responses={
        409: {"description": "Patient Identifier already in use", "model": ErrorMessage}
    },
)
async def create_patient(
    req: Request, name: str = Body(...), id_string: str = Body(...)
) -> PatientResponse:
    """
    Create a patient
    """
    with Session(req.app.state.db) as session:
        patient = (
            session.execute(select(Patient).filter(Patient.id_string == id_string))
            .scalars()
            .first()
        )
        if patient:
            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT,
                content={"message": "Patient Identifier already in use"},
            )

    req.app.state.gcs_client.create_bucket(id_string)
    with Session(req.app.state.db) as session:
        patient = Patient(name=name, id_string=id_string)
        session.add(patient)
        session.commit()

    with Session(req.app.state.db) as session:
        patient = (
            session.execute(select(Patient).filter(Patient.id_string == id_string))
            .scalars()
            .first()
        )
        return patient


@router.delete(
    "/{patient_id}",
    responses={404: {"description": "Patient not found", "model": ErrorMessage}},
)
async def delete_patient(req: Request, patient_id: int) -> PatientResponse:
    """
    Delete a patient by ID
    """
    with Session(req.app.state.db) as session:
        patient = (
            session.execute(select(Patient).filter(Patient.id == patient_id))
            .scalars()
            .first()
        )
        if not patient:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": "Patient not found"},
            )
        req.app.state.gcs_client.get_bucket(patient.id_string).delete()
        session.delete(patient)
        session.commit()
        return patient

@router.get(
    "/{patient_id}/download/{filename}",
    responses={
        404: {"description": "Patient or File not found", "model": ErrorMessage}
    },
)
async def get_patient_file(req: Request, patient_id: int, filename: str) -> bytes:
    """
    Get a file for a patient
    """
    with Session(req.app.state.db) as session:
        patient = (
            session.execute(select(Patient).filter(Patient.id == patient_id))
            .scalars()
            .first()
        )
        if not patient:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": "Patient not found"},
            )
    bucket = req.app.state.gcs_client.get_bucket(patient.id_string)

    filenames = [blob.name for blob in bucket.list_blobs()]
    if filename not in filenames:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "File not found"}
        )

    blob = bucket.blob(filename)
    file_contents = io.BytesIO()
    blob.download_to_file(file_contents)
    file_contents.seek(0)

    return StreamingResponse(file_contents, media_type="application/octet-stream")