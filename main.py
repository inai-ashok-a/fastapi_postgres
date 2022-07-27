from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from config.db import get_db
from models.users import User
from schemas.schema_user import User_req

app = FastAPI()

@app.get('/')
def root():
    return "Hello heroku"

@app.get("/api/users")
def get_by_id( db: Session = Depends(get_db)):
    #return db.query(User).filter(User.id == id).first()
    return db.query(User).all()

