import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from libs.database.engine import SessionMaker


@pytest.fixture()
def session(request):
    session = SessionMaker()
    session.begin_nested()

    def tier_down_session():
        session.rollback()
        session.close()

    request.addfinalizer(tier_down_session)
    return session

