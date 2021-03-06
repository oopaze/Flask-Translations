"""empty message

Revision ID: 61a0bd470285
Revises: 84f0c921ce88
Create Date: 2021-12-14 02:37:54.961670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61a0bd470285'
down_revision = '84f0c921ce88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('estado', sa.Enum('criado', 'iniciado', 'pausado', 'finalizado', name='estado'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'estado')
    # ### end Alembic commands ###
