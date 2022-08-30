from pydantic import BaseModel

class Spot(BaseModel):
    
     
     spotcode:str
     spottype:str
     spotisreserved:bool
     parkid:str