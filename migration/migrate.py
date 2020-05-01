import os
from alembic import config
from alembic import script
from alembic.runtime.migration import MigrationContext
from sqlalchemy import create_engine
from alembic import command

engine = create_engine(os.environ.get('SY_DATABASE_URI'))
alembic_cfg = config.Config('alembic.ini')
script_ = script.ScriptDirectory.from_config(alembic_cfg)


with engine.begin() as conn:
    context = MigrationContext.configure(conn)
    if script_.get_current_head() != context.get_current_revision():
        command.upgrade(alembic_cfg, 'head')