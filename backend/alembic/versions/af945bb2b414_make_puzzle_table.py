"""make puzzle table

Revision ID: af945bb2b414
Revises: 28267285b4a9
Create Date: 2024-04-13 21:40:57.344222

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af945bb2b414'
down_revision: Union[str, None] = '28267285b4a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'puzzles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('patient_id', sa.Integer, sa.ForeignKey('patients.id', ondelete="CASCADE"), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('filename', sa.String(100), nullable=False),
        sa.UniqueConstraint('patient_id', 'name', name='uq_puzzles_patient_id_name'),
    )

def downgrade() -> None:
    op.drop_table('puzzles')