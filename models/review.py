from pydantic import BaseModel

class Review(BaseModel):
    
     note:float
     parkid:str
     comment:str
     clientid:str
     