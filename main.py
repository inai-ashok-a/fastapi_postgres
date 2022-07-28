from fastapi import FastAPI, Depends,status
from sqlalchemy.orm import Session
from config.db import get_db
from models.users import User
from schemas.schema_user import User_req
from email_validator import validate_email,EmailNotValidError


app = FastAPI()

@app.get('/')
def root():
    return "Hello heroku from Ashok!!!"

@app.get("/api/users")
def get_all_users( db: Session = Depends(get_db)):
    #return db.query(User).filter(User.id == id).first()
    return db.query(User).all()


@app.post('/api/users',status_code=status.HTTP_201_CREATED)
def create_an_user( obj:User_req,db: Session = Depends(get_db)):
     val_email = obj.email

     try:
         val_email = validate_email(val_email).email
     except EmailNotValidError as e:
         return "Please enter valid Email! :("

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


@app.put('/api/users/{user_id}',status_code=status.HTTP_200_OK)
def update_an_item(user_id:int,obj:User_req,db: Session = Depends(get_db)):
    field_to_update=db.query(User).filter(User.id==user_id).first()

    if field_to_update is None:
        return "Sry !! No User with this id"

    field_to_update.name=obj.name
    field_to_update.age=obj.age

    db.commit()

    return db.query(User).all()