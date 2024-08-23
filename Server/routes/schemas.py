from pydantic import BaseModel

# --types--
from datetime import date
from typing import List


class Product(BaseModel):
    name: str
    price: float | int 
    quantity: int
    order_status: str
    start_time_order: date
    
    class client:
        email: str
        phone: str | int
        city: str
        street: str
        house: str
        building: str
        apartament: str
        code_intercome: str | int
        comment: str

class Order(BaseModel):
    products: List[Product] 
    
    