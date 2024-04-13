from .base import Base

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

class Pair(Base):
    __tablename__ = 'object_pairs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    patient_id: Mapped[int] = mapped_column(Integer, ForeignKey('patients.id'), nullable=False)
    object_one_type: Mapped[str] = mapped_column(String(100), nullable=False)
    object_one_value: Mapped[str] = mapped_column(String(100), nullable=False)
    object_two_type: Mapped[str] = mapped_column(String(100), nullable=False)
    object_two_value: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self) -> str:
        return f'Pair({self.id}, {self.patient_id}, {self.object_one_type}, {self.object_one_value}, {self.object_two_type}, {self.object_two_value})'
    
    def __str__(self) -> str:
        return f'Pair({self.id}, {self.patient_id}, {self.object_one_type}, {self.object_one_value}, {self.object_two_type}, {self.object_two_value})'