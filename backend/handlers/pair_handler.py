from typing import List, Union

from fastapi import APIRouter, Form, Request, UploadFile, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.error import ErrorMessage
from models.pair import Pair, PairResponse
from models.patient import Patient

from utils.storage import delete_file, upload_file

router = APIRouter(prefix="/pair", tags=["content"])


@router.get("/")
async def get_pairs(request: Request) -> List[PairResponse]:
    """
    Get all pairs
    """
    with Session(request.app.state.db) as session:
        return session.execute(select(Pair)).scalars().all()


@router.get("/{pair_id}", responses={404: {"description": "Pair not found", "model": ErrorMessage}})
async def get_pair_by_id(req: Request, pair_id: int) -> PairResponse:
    """
    Get a pair by ID
    """
    with Session(req.app.state.db) as session:
        pair = (
            session.execute(select(Pair).filter(Pair.id == pair_id)).scalars().first()
        )
        if not pair:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": "Pair not found"},
            )
        return pair

@router.get(
    "/patient/{patient_id}",
    responses={404: {"description": "Patient not found", "model": ErrorMessage}},
)
async def get_pairs_by_patient_id(req: Request, patient_id: int) -> List[PairResponse]:
    """
    Get all pairs for a patient
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

        return (
            session.execute(select(Pair).filter(Pair.patient_id == patient_id))
            .scalars()
            .all()
        )

@router.post(
    "/{patient_id}",
    responses={404: {"description": "Patient not found", "model": ErrorMessage}},
)
async def make_pair(
    req: Request,
    patient_id: int,
    object_one_value: Union[str, UploadFile] = Form(...),
    object_two_value: Union[str, UploadFile] = Form(...),
) -> PairResponse:
    """
    Create a pair for a patient
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

    if isinstance(object_one_value, str):
        type_one = "string"
        value_one = object_one_value
    else:
        type_one = "file"
        value_one = upload_file(
            req.app.state.gcs_client, patient.id_string, object_one_value
        )

    if isinstance(object_two_value, str):
        type_two = "string"
        value_two = object_two_value
    else:
        type_two = "file"
        value_two = upload_file(
            req.app.state.gcs_client, patient.id_string, object_two_value
        )

    with Session(req.app.state.db) as session:
        pair = Pair(
            patient_id=patient_id,
            object_one_type=type_one,
            object_one_value=value_one,
            object_two_type=type_two,
            object_two_value=value_two,
        )
        session.add(pair)
        session.flush()
        pair_id = pair.id
        session.commit()

    with Session(req.app.state.db) as session:
        pair = (
            session.execute(select(Pair).filter(Pair.id == pair_id)).scalars().first()
        )
        return pair

@router.delete(
    "/{pair_id}",
    responses={
        404: {"description": "Patient or Pair not found", "model": ErrorMessage}
    },
)
async def delete_pair(req: Request, pair_id: int) -> PairResponse:
    """
    Delete a pair by ID
    """
    with Session(req.app.state.db) as session:
        pair = (
            session.execute(select(Pair).filter(Pair.id == pair_id)).scalars().first()
        )
        patient = (
            session.execute(select(Patient).filter(Patient.id == pair.patient_id))
            .scalars()
            .first()
        )
        if not patient:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": "Patient not found"},
            )
        if not pair:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": "Pair not found"},
            )
        if pair.object_one_type == "file":
            delete_file(
                req.app.state.gcs_client, patient.id_string, pair.object_one_value
            )
        if pair.object_two_type == "file":
            delete_file(
                req.app.state.gcs_client, patient.id_string, pair.object_two_value
            )
        session.delete(pair)
        session.commit()
        return pair
