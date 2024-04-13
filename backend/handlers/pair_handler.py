from fastapi import APIRouter, Request, UploadFile, File, Form
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Union

from models.pair import Pair
from models.patient import Patient

router = APIRouter(prefix="/pair", tags=["content"])

@router.get("/")
async def get_pairs(request: Request):
    with Session(request.app.state.db) as session:
        return session.execute(select(Pair)).scalars().all()

@router.get("/{patient_id}")
async def get_pairs_by_patient_id(req: Request, patient_id: int):
    with Session(req.app.state.db) as session:
        return session.execute(select(Pair).filter(Pair.patient_id == patient_id)).scalars().all()

@router.get("/{patient_id}/{filename}")
async def get_file(req: Request, patient_id: int, filename: str):
    with Session(req.app.state.db) as session:
        patient = session.execute(select(Patient).filter(Patient.id == patient_id)).scalars().first()
        if not patient:
            return "Patient not found"
    bucket = req.app.state.gcs_client.get_bucket(patient.id_string)
    blob = bucket.blob(filename)
    return blob.download_as_string()

def upload_file(gcs_client, patient_id, file):
    bucket = gcs_client.get_bucket(patient_id)
    filenames = [blob.name for blob in bucket.list_blobs()]
    i = 0
    original_filename = file.filename
    while file.filename in filenames:
        file.filename = f'{i}_{original_filename}'
        i += 1
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file.file)
    return file.filename

@router.post("/{patient_id}")
async def make_pair(req: Request, patient_id: int, object_one_value: Union[str, UploadFile] = Form(...), object_two_value: Union[str, UploadFile] = Form(...)):
    with Session(req.app.state.db) as session:
        patient = session.execute(select(Patient).filter(Patient.id == patient_id)).scalars().first()
        if not patient:
            return "Patient not found"
    
    if isinstance(object_one_value, str):
        type_one = "string"
        value_one = object_one_value
    else:
        type_one = "file"
        value_one = upload_file(req.app.state.gcs_client, patient.id_string, object_one_value)
    
    if isinstance(object_two_value, str):
        type_two = "string"
        value_two = object_two_value
    else:
        type_two = "file"
        value_two = upload_file(req.app.state.gcs_client, patient.id_string, object_two_value)
    
    with Session(req.app.state.db) as session:
        pair = Pair(patient_id=patient_id, object_one_type=type_one, object_one_value=value_one, object_two_type=type_two, object_two_value=value_two)
        session.add(pair)
        session.commit()
        return pair

def delete_file(gcs_client, patient_id, filename):
    bucket = gcs_client.get_bucket(patient_id)
    blob = bucket.blob(filename)
    blob.delete()

@router.delete("/{pair_id}")
async def delete_pair(req: Request, pair_id: int):
    with Session(req.app.state.db) as session:
        pair = session.execute(select(Pair).filter(Pair.id == pair_id)).scalars().first()
        patient = session.execute(select(Patient).filter(Patient.id == pair.patient_id)).scalars().first()
        if pair.object_one_type == "file":
            delete_file(req.app.state.gcs_client, patient.id_string, pair.object_one_value)
        if pair.object_two_type == "file":
            delete_file(req.app.state.gcs_client, patient.id_string, pair.object_two_value)
        session.delete(pair)
        session.commit()
        return pair