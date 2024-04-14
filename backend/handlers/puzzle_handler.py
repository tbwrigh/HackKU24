from fastapi import APIRouter, Request, status, UploadFile, File, Form
from fastapi.responses import JSONResponse

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.error import ErrorMessage
from models.puzzle import Puzzle, PuzzleResponse
from models.patient import Patient

from utils.storage import upload_file, delete_file

from typing import List

router = APIRouter(prefix="/puzzle", tags=["content"])

@router.get("/")
async def get_puzzles(request: Request) -> List[PuzzleResponse]:
    """
    Get all puzzles
    """
    with Session(request.app.state.db) as session:
        return session.execute(select(Puzzle)).scalars().all()
    
@router.get("/{puzzle_id}", responses={404: {"description": "Puzzle not found", "model": ErrorMessage}})
async def get_puzzle_by_id(req: Request, puzzle_id: int) -> PuzzleResponse:
    """
    Get a puzzle by ID
    """
    with Session(req.app.state.db) as session:
        puzzle = (
            session.execute(select(Puzzle).filter(Puzzle.id == puzzle_id)).scalars().first()
        )
        if not puzzle:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": "Puzzle not found"},
            )
        return puzzle

@router.get("/patient/{patient_id}", responses={404: {"description": "Patient not found", "model": ErrorMessage}})
async def get_puzzles_by_patient_id(req: Request, patient_id: int) -> List[PuzzleResponse]:
    """
    Get all puzzles for a patient
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
            session.execute(select(Puzzle).filter(Puzzle.patient_id == patient_id))
            .scalars()
            .all()
        )
    
@router.post("/{patient_id}", responses={404: {"description": "Patient not found", "model": ErrorMessage}})
async def create_puzzle(req: Request, patient_id: int, name: str = Form(...), file: UploadFile = File(...)) -> PuzzleResponse:
    """
    Create a puzzle
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

        filename = upload_file(req.app.state.gcs_client, patient.id_string, file)
        puzzle = Puzzle(patient_id=patient_id, name=name, filename=filename)
        session.add(puzzle)
        session.flush()
        puzzle_id = puzzle.id
        session.commit()

    with Session(req.app.state.db) as session:
        puzzle = (
            session.execute(select(Puzzle).filter(Puzzle.id == puzzle_id)).scalars().first()
        )
        return puzzle

@router.delete("/{puzzle_id}", responses={404: {"description": "Puzzle not found", "model": ErrorMessage}})
async def delete_puzzle(req: Request, puzzle_id: int) -> PuzzleResponse:
    """
    Delete a puzzle
    """
    with Session(req.app.state.db) as session:
        puzzle = (
            session.execute(select(Puzzle).filter(Puzzle.id == puzzle_id)).scalars().first()
        )
        if not puzzle:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": "Puzzle not found"},
            )
        delete_file(req.app.state.gcs_client, puzzle.patient_id, puzzle.filename)
        session.delete(puzzle)
        session.commit()
        return puzzle