"""0817_dormant

Revision ID: 11568915fcb2
Revises: df28c41a8200
Create Date: 2020-08-17 20:06:46.636602

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import LaboratoryTypes
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '11568915fcb2'
down_revision = 'df28c41a8200'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('hearts_ibfk_1', 'hearts', type_='foreignkey')
    op.drop_constraint('hearts_ibfk_2', 'hearts', type_='foreignkey')
    op.create_foreign_key(None, 'hearts', 'users', ['to_user_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'hearts', 'users', ['from_user_id'], ['id'], ondelete='SET NULL')
    op.add_column('mbti_results', sa.Column('result_rate', mysql.JSON(), nullable=True))
    op.add_column('users', sa.Column('dormant_at', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'dormant_at')
    op.drop_column('mbti_results', 'result_rate')
    op.drop_constraint(None, 'hearts', type_='foreignkey')
    op.drop_constraint(None, 'hearts', type_='foreignkey')
    op.create_foreign_key('hearts_ibfk_2', 'hearts', 'users', ['to_user_id'], ['id'])
    op.create_foreign_key('hearts_ibfk_1', 'hearts', 'users', ['from_user_id'], ['id'])
    # ### end Alembic commands ###
