import os
from datetime import datetime
from flask import g
from sqlalchemy import create_engine, types, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 어짜피 database 주소는 도커 파일에서 넣을 수가 없다... 다른 컨테이너에서 돌기 때문.
# conn_args = { 'ssl_args': os.environ.get('SSL_CA_PATH') } if os.environ.get('STAGE') == 'PRODUCTION' else {}
engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'), pool_recycle=300)
SessionMaker = sessionmaker(bind=engine)


def set_session_destroyer(app):
    '''
    app 설정 단계에서 반드시 한 번 호출해 주어야 합니다.
    이 함수를 호출하지 않았다면 Session() 함수로 인해 생성된 session 연결이
    끊어지지 않고 계속 남아, QueuePool 을 가득 채우게 됩니다. (꽉 차면 더 이상 sql alchemy 못 씀)
    '''
    @app.teardown_appcontext
    def close_session(exc):
        '''
        None 이 전달되는데 뭔지 모르겠네 문서에도 없고.
        '''
        if 'session' in g:
            if g.session_changed is True:
                g.session.commit()
            g.session.close()


def Session(changed=False, committed=False):
    '''
    g 에 등록된 세션을 리턴하는 헬퍼함수
    '''
    if 'session' not in g:
        g.session = SessionMaker()
        g.session_changed = False # session 을 처음 만들때 False 로
    if changed is True:
        g.session_changed = True
    if committed is True:
        g.session_changed = False

    return g.session


def afr(*args):
    '''
    auto add flush return
    '''
    Session(changed=True).add_all(args)
    Session().flush()

    if len(args) == 1:
        return args[0]

    return args


class Base:
    '''
    https://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/mixins.html
    '''
    id = Column(Integer, primary_key=True, autoincrement=True)


    def json(self, **kwargs):
        return {}


Base = declarative_base(cls=Base)


class LaboratoryTypes:


    class TextTuple(types.TypeDecorator):
        '''
        db 에 들어갈 때에는 , 를 포함한 문자열로 들어가며
        db 에서 나올 때에는 튜플로 빠져나오는 자료형입니다.

        주의! 증강 타입은 mutability 를 인식하지 못합니다!
        http://docs.sqlalchemy.org/en/latest/core/custom_types.html
        따라서 리스트가 아닌 튜플을 사용했습니다.

        주의! 콤마가 들어있는 문자열을 튜플 안에 집어넣지 마시오
        '''
        impl = types.TEXT

        def process_bind_param(self, value, dialect):
            return ','.join(map(str, value)) if value else ''

        def process_result_value(self, value, dialect):
            return tuple((item for item in value.split(',')) if value else () )


    class IntTuple(types.TypeDecorator):
        '''
        db로부터 나올 때에는 Integer 로 이루어진 튜플!
        '''
        impl = types.TEXT

        def process_bind_param(self, value, dialect):
            return ','.join(map(str, value)) if value else ''

        def process_result_value(self, value, dialect):
            return tuple((int(item) for item in value.split(',') if value))


    class TextDate(types.TypeDecorator):

        impl = types.DATE

        def process_bind_param(self, value, dialect):
            return datetime.strptime(value, '%Y-%m-%d').date()

        def process_result_value(self, value, dialect):
            return value


    class TextTime(types.TypeDecorator):

        impl = types.TIME

        def process_bind_param(self, value, dialect):
            return datetime.strptime(value, '%H:%M:%S').time()

        def process_result_value(self, value, dialect):
            return value


    class TextDateTime(types.TypeDecorator):

        impl = types.DATETIME

        def process_bind_param(self, value, dialect):
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')

        def process_result_value(self, value, dialect):
            return value



