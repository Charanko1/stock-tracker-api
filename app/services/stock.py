from app.core.exceptions import NotFoundException, BadRequestException
from app.models.stock import Stock
from app.repositories.stock import StockRepository
from app.schemas.stock import StockCreate

class StockService:
    def __init__(self, stock_repo: StockRepository):
        self.stock_repo = stock_repo

    def create(self, stock_data: StockCreate) -> Stock:
        ticker_upper = stock_data.ticker.upper()
        existing_stock = self.stock_repo.get_by_ticker(ticker_upper)
        if existing_stock:
            raise BadRequestException(message=f"Saham dengan ticker {ticker_upper} sudah ada")

        new_stock = Stock(
            ticker=ticker_upper,
            company_name=stock_data.company_name,
            sector=stock_data.sector
        )  

        return self.stock_repo.create(new_stock)

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Stock]:
        stock = self.stock_repo.get_all(skip=skip, limit=limit)

    def get_by_id(self, stock_id: int) -> Stock:
        stock = self.stock_repo.get_by_id(stock_id)
        if not stock:
            raise NotFoundException(message="Saham tidak ditemukan")
        return stock