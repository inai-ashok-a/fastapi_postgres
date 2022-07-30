from fastapi import FastAPI, Depends,status,HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from models.users import User
from schemas.schema_user import User_req
from email_validator import validate_email,EmailNotValidError
from auth.util import get_hashed_password,verify_password
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login"
)


app = FastAPI()

@app.get('/')
def root():
    return "Hello heroku from Ashok!!!"


user_email="user_email"

@app.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = (user.password)
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    global user_email
    user_email=user.email
    return user.name



@app.get("/api/users")
def get_all_users(users: User_req = Depends(reuseable_oauth), db: Session = Depends(get_db)):
    return db.query(User).filter(User.email == user_email).first()


@app.post('/api/users',status_code=status.HTTP_201_CREATED)
def create_an_user( obj:User_req,db: Session = Depends(get_db)):
     val_email = obj.email

     try:
         val_email = validate_email(val_email).email
     except EmailNotValidError as e:
         return "Please enter valid Email! :("

     db_user_mail = db.query(User).filter(User.email == obj.email).first()

     if db_user_mail is not None:
         return "Mail already found!!!"

     db_user_id = db.query(User).filter(User.id == obj.id).first()

     if db_user_id is not None:
         return "Your user Id already found!!!"

     if obj.password.__len__()<6:
         return "Password is very short!:("

     new_user = User(

        name=obj.name,
        email=obj.email,
        age=obj.age,
        password=get_hashed_password(obj.password)
        )

     db.add(new_user)
     db.commit()

     return db.query(User).all()


@app.put('/api/users/{user_id}',status_code=status.HTTP_200_OK)
def update_an_user(user_id:int,obj:User_req,db: Session = Depends(get_db),users: User_req = Depends(reuseable_oauth)):
    field_to_update=db.query(User).filter(User.id==user_id).first()

    if field_to_update is None:
        return "Sry !! No User with this id"

    field_to_update.name=obj.name
    field_to_update.age=obj.age

    db.commit()

    return db.query(User).filter(User.id==user_id).first()


@app.delete('/api/users/{user_id}')
def delete_user(user_id: int,db: Session = Depends(get_db),users: User_req = Depends(reuseable_oauth)):
    user_to_delete = db.query(User).filter(User.id == user_id).first()

    if user_to_delete is None:
        return "Sry !! No user with this id...:("

    db.delete(user_to_delete)
    db.commit()

    return "Successfully deleted!!!"