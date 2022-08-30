from datetime import date, datetime
from pydantic import BaseModel
from datetime import datetime
class Reservation(BaseModel):
    
    clientId: str
    spotId: str
    startDate: datetime
    endDate: datetime
    value:float
    isPaid: bool
    parkName:str
    spotType:str
    parkId:str
    carNumber:str