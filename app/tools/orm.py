import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.configs import db_configs


class ORM:

    @classmethod
    def db(cls):
        db_uri = 'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{name}'.format(**db_configs)
        engine = create_engine(
            db_uri,
            encoding='utf-8',
            echo=False,  # 是否打印日志
            pool_size=100,  # 最大连接数
            pool_recycle=10,  # 连接最大持续时间
            connect_args={'charset': 'utf8'}
        )
        
        Session = sessionmaker(
            bind=engine,
            autocommit=False,  # 是否自动提交
            autoflush=True,  # 自动刷新权限
            expire_on_commit=False,
        )

        return Session()
