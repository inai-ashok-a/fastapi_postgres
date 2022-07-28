from config.db import Base
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    age = Column(Integer,nullable=False)