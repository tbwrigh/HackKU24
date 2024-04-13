from .base import Base

from pydantic import BaseModel
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped

class Patient(Base):
    __tablename__ = 'patients'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    id_string: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self) -> str:
        return f'Patient({self.id}, {self.name}, {self.id_string})'
    
    def __str__(self) -> str:
        return f'Patient({self.id}, {self.name}, {self.id_string})'
    
class PatientResponse(BaseModel):
    id: int
    name: str
    id_string: str