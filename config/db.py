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

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Ashoksql@localhost/postgres"
SQLALCHEMY_DATABASE_URL="postgres://nczwkidqlblvsr:f17ab2bc05181a3b9eaab4cb3292f319d5c9d0e246d873c25b5a341c2ceaa65c@ec2-44-208-88-195.compute-1.amazonaws.com:5432/d84n6ro659q12n"

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