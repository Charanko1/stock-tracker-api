from sqlalchemy.orm import Session
from app.models.stock import Stock

class StockRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, stock: Stock) -> Stock:
        self.db.add(stock)
        self.db.commit()
        self.db.refresh(stock)
        return stock

    def get_by_ticker(self, ticker : str) -> Stock | None:
        return self.db.query(Stock).filter(Stock.ticker == ticker).first()

    def get_by_id(self, stock_id : int) -> Stock | None :
        return self.db.query(Stock).filter(Stock.id == stock_id).first()

    def get_all(self, skip : int = 0, limit : int = 100) -> list[Stock] :
        return self.db.query(Stock).offset(skip).limit(limit).all()

