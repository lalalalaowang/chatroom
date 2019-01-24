from sqlalchemy.dialects.mysql import TINYINT, INTEGER, VARCHAR, DATETIME, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column

Base = declarative_base()
metadata = Base.metadata


class Video(Base):

    __tablename__ = 'video'

    id = Column(INTEGER, primary_key=True, )
    name = Column(VARCHAR(255), nullable=False)
    url = Column(VARCHAR(255), nullable=False)
    logo = Column(VARCHAR(255), nullable=False)
    createAt = Column(DATETIME, nullable=False)
    updateAt = Column(DATETIME, nullable=False)


class Msg(Base):

    __tablename__ = 'msg'

    id = Column(INTEGER, primary_key=True)
    content = Column(TEXT)
    createAt = Column(DATETIME, nullable=False)
    updateAt = Column(DATETIME, nullable=False)


class User(Base):

    __tablename__ = 'user'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(20), unique=True, nullable=False)
    pwd = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(100), unique=True, nullable=False)
    phone = Column(VARCHAR(11), unique=True, nullable=False)
    sex = Column(TINYINT)
    constellation = Column(TINYINT)
    face = Column(VARCHAR(255))
    info = Column(VARCHAR(255))
    createAt = Column(DATETIME, nullable=False)
    updateAt = Column(DATETIME, nullable=False)


if __name__ == "__main__":
    from mysql import connector
    from sqlalchemy import create_engine
    db_configs = dict(
        host='127.0.0.1',
        port='3306',
        name='chatroom',
        user='root',
        password='111222aA',
    )
    db_uri = 'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{name}'.format(**db_configs)
    engine = create_engine(db_uri,encoding='utf-8',echo=True)
    metadata.create_all(engine)
