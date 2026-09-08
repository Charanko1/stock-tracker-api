from fastapi import APIRouter
from app.api.v1.endpoints import portfolio, stock, user

api_router = APIRouter()
api_router.include_router(user.router)
api_router.include_router(stock.router)
api_router.include_router(portfolio.router)