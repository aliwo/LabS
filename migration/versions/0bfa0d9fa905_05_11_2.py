"""05_11_2

Revision ID: 0bfa0d9fa905
Revises: 1d4e321d5999
Create Date: 2020-05-11 15:40:20.831293

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import LaboratoryTypes
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0bfa0d9fa905'
down_revision = '1d4e321d5999'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('nick_name', mysql.CHAR(length=50), nullable=True))
    op.drop_index('name', table_name='users')
    op.create_unique_constraint(None, 'users', ['nick_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.create_index('name', 'users', ['name'], unique=True)
    op.drop_column('users', 'nick_name')
    # ### end Alembic commands ###