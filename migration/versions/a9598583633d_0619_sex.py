"""0619_sex

Revision ID: a9598583633d
Revises: f2abe176ea17
Create Date: 2020-06-19 16:54:45.422654

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import LaboratoryTypes
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a9598583633d'
down_revision = 'f2abe176ea17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('matches',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('from_user_id', sa.Integer(), nullable=True),
    sa.Column('to_user_id', sa.Integer(), nullable=True),
    sa.Column('matched', sa.BOOLEAN(), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('matched_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['from_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['to_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_matches_from_user_id'), 'matches', ['from_user_id'], unique=False)
    op.create_index(op.f('ix_matches_to_user_id'), 'matches', ['to_user_id'], unique=False)
    op.add_column('users', sa.Column('sex', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'sex')
    op.drop_index(op.f('ix_matches_to_user_id'), table_name='matches')
    op.drop_index(op.f('ix_matches_from_user_id'), table_name='matches')
    op.drop_table('matches')
    # ### end Alembic commands ###
