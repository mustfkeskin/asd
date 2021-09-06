from pydantic import BaseModel
from typing import List

class Add2CartEvent(BaseModel):
    event: str 
    sessionid: str 
    eventtime: str 
    price: float
    productid:str

class SessionAdd2CardEvents(BaseModel):
    events: List[Add2CartEvent] = []
