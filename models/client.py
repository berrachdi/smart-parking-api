
from pydantic import BaseModel

class Client(BaseModel):
    
    fullname: str
    email: str
    phonenumber: str
    password: str
    isValidate: bool
    
    


    
   