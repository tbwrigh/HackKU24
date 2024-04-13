from pydantic import BaseModel
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    id_string: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self) -> str:
        return f"Patient({self.id}, {self.name}, {self.id_string})"

    def __str__(self) -> str:
        return f"Patient({self.id}, {self.name}, {self.id_string})"


class PatientResponse(BaseModel):
    id: int
    name: str
    id_string: str
