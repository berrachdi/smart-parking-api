from pydantic import BaseModel

class Pricing(BaseModel):
    
    normalPricing:str
    extraPricing:str
    parkId:str