"""empty message

Revision ID: 714256bfd26c
Revises: 
Create Date: 2023-09-25 14:18:55.738353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '714256bfd26c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### Stores_app Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### Stores_app Alembic commands ###
