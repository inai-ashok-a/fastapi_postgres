# from sqlalchemy import create_engine,MetaData
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
#
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Ashoksql@localhost/users"
#
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# meta=MetaData()
#
# Base = declarative_base()
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     except:
#         db.close()
#
# # from sqlalchemy import create_engine,MetaData
# #
# # engine=create_engine('postgresql://postgres:Ashoksql@localhost/users')
# # meta=MetaData()
# # con=engine.connect()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Ashoksql@localhost/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()