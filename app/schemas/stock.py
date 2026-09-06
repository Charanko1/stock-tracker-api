from pydantic import BaseModel

class StockBase(BaseModel):
    ticker : str
    company_name : str
    sector : str

class StockCreate(StockBase):
    pass

class StockResponse(StockBase):
    id : int

    class Config :
        from_attributes = True
