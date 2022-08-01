from config.db import Base
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String


class User(Base):
    __tablename__ = 'user_data'


    name = Column(String, nullable=False)
    email = Column(String, primary_key=True)
    age = Column(Integer,nullable=False)
    password=Column(String,nullable=False)