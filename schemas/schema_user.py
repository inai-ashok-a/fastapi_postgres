from pydantic import BaseModel


class User_req(BaseModel):
    id:int =123
    name:str
    email:str
    age:int
    password:str
    #
    class Config:
        orm_mode=True

