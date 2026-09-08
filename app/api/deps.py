from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.Session import get_db
from app.repositories import UserRepository, StockRepository, PortfolioRepository
from app.services import UserService, StockService, PortofolioService

def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

def get_user_service(repo: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(repo)

def get_stock_repository(db: Session = Depends(get_db)) -> StockRepository:
    return StockRepository(db)

def get_stock_service(repo : StockRepository = Depends(get_stock_repository)) -> StockService:
    return StockService(repo)

def get_portfolio_repository(db : Session = Depends(get_db)) -> PortfolioRepository:
    return StockRepository(db)

def get_portfolio_service(repo : PortofolioService = Depends(get_user_repository)) -> PortofolioService:
    return PortofolioService(repo)

