from fastapi import APIRouter, Depends, status, Query
from app.api.deps import get_portfolio_service
from app.schemas.portfolio import PortfolioCreate, PortfolioResponse
from app.services import PortfolioService

router = APIRouter(prefix="/portfolio", tags=["Portfolios"])

@router.post("/", response_model=PortfolioResponse, status_code=status.HTTP_201_CREATED)
def add_portfolio(
    portfolio_data : PortfolioCreate,
    user_id : int = Query(..., description="ID user pemilik transaksi"),
    portfolio_service : PortfolioService = Depends(get_portfolio_service)
):
    return portfolio_service.add_to_portfolio(user_id=user_id, portfolio_data=portfolio_data)

@router.get("/user/{user_id}", response_model=list[PortfolioResponse])
def get_user_portfolio(
    user_id : int,
    portfolio_service : PortfolioService = Depends(get_portfolio_service)
):
    return portfolio_service.get_user_portfolio(user_id=user_id)

@router.delete("/{portfolio_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_stock(
    portfolio_id : int,
    portfolio_service : PortfolioService = Depends(get_portfolio_service)
): 
    return portfolio_service.remove_from_portfolio(portfolio_id)