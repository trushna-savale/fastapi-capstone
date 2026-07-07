#Keeps pydantic models for organization
from pydantic import BaseModel #pydantic= data validator

class User(BaseModel):  #creating blueprint for data
    name: str
    age: int