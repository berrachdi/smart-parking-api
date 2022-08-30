from pydantic import BaseModel

class Park(BaseModel):
    
     parkname:str
     parkaddress:str
     maps:list
     city:str
     surface:float
     note:float
     