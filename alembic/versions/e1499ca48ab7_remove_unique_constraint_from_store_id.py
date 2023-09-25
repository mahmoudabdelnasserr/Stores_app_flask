"""remove_unique_constraint_from_store_id

Revision ID: e1499ca48ab7
Revises: 5d596c41f15a
Create Date: 2023-09-25 10:33:42.782138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1499ca48ab7'
down_revision: Union[str, None] = '5d596c41f15a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
