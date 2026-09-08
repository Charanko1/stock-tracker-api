from pydantic import BaseModel
from datetime import datetime
from .stock import StockResponse

class PortfolioBase(BaseModel):
    stock_id : int
    lots : int
    average_price : float

class PortfolioCreate(PortfolioBase):
    pass

class PortfolioResponse(PortfolioBase):
    id : int
    user_id : int
    created_at : datetime
    stock : StockResponse

    class Config :
        from_attributes = True
