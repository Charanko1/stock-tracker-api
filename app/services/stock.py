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
            raise BadRequestException(message="Saham dengan ticker {ticker_upped} sudah ada")

        new_stock = Stock(
            ticker=ticker_upper,
            company_name=stock_data.company_name,
            sector=stock_data.sector
        )  

        return self.stock_repo.create(new_stock)