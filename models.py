from pydantic import BaseModel

class UserCreate(BaseModel):
    username:str
    password:str
    role:str
    email:str

class UserLogin(BaseModel) :
    username:str
    password:str
    
