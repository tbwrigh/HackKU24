from pydantic import BaseModel
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Pair(Base):
    __tablename__ = "object_pairs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    patient_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("patients.id", ondelete="CASCADE"), nullable=False
    )
    object_one_type: Mapped[str] = mapped_column(String(100), nullable=False)
    object_one_value: Mapped[str] = mapped_column(String(100), nullable=False)
    object_two_type: Mapped[str] = mapped_column(String(100), nullable=False)
    object_two_value: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self) -> str:
        return f"Pair({self.id}, {self.patient_id}, {self.object_one_type}, {self.object_one_value}, {self.object_two_type}, {self.object_two_value})"

    def __str__(self) -> str:
        return f"Pair({self.id}, {self.patient_id}, {self.object_one_type}, {self.object_one_value}, {self.object_two_type}, {self.object_two_value})"


class PairResponse(BaseModel):
    id: int
    patient_id: int
    object_one_type: str
    object_one_value: str
    object_two_type: str
    object_two_value: str
