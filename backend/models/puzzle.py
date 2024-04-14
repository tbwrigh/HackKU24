from sqlalchemy import Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from pydantic import BaseModel

from .base import Base

class Puzzle(Base):
    __tablename__ = "puzzles"
    __table_args__ = (
        UniqueConstraint('patient_id', 'name', name='uq_puzzles_patient_id_name'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    patient_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    filename: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self) -> str:
        return f"Puzzle({self.id}, {self.patient_id}, {self.name}, {self.filename})"

    def __str__(self) -> str:
        return f"Puzzle({self.id}, {self.patient_id}, {self.name}, {self.filename})"
    
class PuzzleResponse(BaseModel):
    id: int
    patient_id: int
    name: str
    filename: str