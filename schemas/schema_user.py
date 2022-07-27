from pydantic import BaseModel


class User_req(BaseModel):
    id:int
    name:str
    email:str
    age:int
