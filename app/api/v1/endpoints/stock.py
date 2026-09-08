from fastapi import APIRouter, Depends, Query, status
from app.api.deps import get_stock_service
from app.schemas.stock import StockCreate, StockResponse
from app.services import StockService

router = APIRouter(prefix="/stocks", tags=["Stocks"])

@router.post("/", reponse_model=StockResponse, status_code=status.HTTP_201_CREATED)
def create_stock(
    stock_data : StockCreate,
    stock_service : StockService = Depends(get_stock_service)
):
    return stock_service.create(stock_data)

@router.get("/", response_model=StockResponse)
def get_stocks(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    stock_service : StockService = Depends(get_stock_service)
):
    return stock_service.get_all(skip=skip,limit=limit)

@router.get("/{stock_id}", response_model=StockResponse)
def get_stock(
    stock_id : int,
    stock_service : StockService = Depends(get_stock_service)
): 
    return stock_service.get_by_id(stock_id)
