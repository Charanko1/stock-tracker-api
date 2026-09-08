from sqlalchemy.orm import Session
from app.models.portfolio import Portfolio

class PortfolioRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, portfolio: Portfolio) -> Portfolio:
        self.db.add(portfolio)
        self.db.commit()
        self.db.refresh(portfolio)
        return portfolio

    def get_by_user_id(self, user_id : int) -> list[Portfolio]:
        return self.db.query(Portfolio).filter(Portfolio.user_id == user_id).all()

    def get_by_id(self, portfolio_id :int) -> Portfolio:
        return self.db.query(Portfolio).filter(Portfolio.id == portfolio_id).first()

    def delete(self, portfolio: Portfolio) -> None:
        self.db.delete(portfolio)
        self.db.commit()