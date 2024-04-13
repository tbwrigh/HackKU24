"""intial table

Revision ID: 28267285b4a9
Revises: 
Create Date: 2024-04-12 23:55:50.366019

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28267285b4a9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'patients',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('id_string', sa.String(100), nullable=False),
    )
    op.create_table(
        'object_pairs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('patient_id', sa.Integer, sa.ForeignKey('patients.id'), nullable=False),
        sa.Column('object_one_type', sa.String(100), nullable=False),
        sa.Column('object_one_value', sa.String(100), nullable=False),
        sa.Column('object_two_type', sa.String(100), nullable=False),
        sa.Column('object_two_value', sa.String(100), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('object_pairs')
    op.drop_table('patients')
