from fastapi import FastAPI, Depends,status
from sqlalchemy.orm import Session
from config.db import get_db
from models.users import User
from schemas.schema_user import User_req


app = FastAPI()

@app.get('/')
def root():
    return "Hello heroku from Ashok!!!"

@app.get("/api/users")
def get_by_id( db: Session = Depends(get_db)):
    #return db.query(User).filter(User.id == id).first()
    return db.query(User).all()


@app.post('/items',status_code=status.HTTP_201_CREATED)
def create_an_item( obj:User_req,db: Session = Depends(get_db)):

     db_item = db.query(User).filter(User.email == obj.email).first()

     if db_item is not None:
         return "Mail already found!!!"

     new_user = User(
        id=obj.id,
        name=obj.name,
        email=obj.email,
        age=obj.age
        )

     db.add(new_user)
     db.commit()

     return db.query(User).all()