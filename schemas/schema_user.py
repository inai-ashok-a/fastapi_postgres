from pydantic import BaseModel


class User_req(BaseModel):


    name:str
    email:str
    age:int
    password:str
    #
    class Config:
        orm_mode=True

