from app.core.exceptions import NotFoundException, BadRequestException, ForbiddenException
from app.models.portfolio import Portfolio
from app.repositories.portfolio import PortfolioRepository
from app.repositories.stock import StockRepository
from app.schemas.portfolio import PortfolioCreate

class PortfolioService:
    def __init__(self, portfolio_repo : PortfolioRepository, stock_repo : StockRepository):
        self.portfolio_repo = portfolio_repo
        self.stock_repo = stock_repo

    def add_to_portfolio(self, user_id: int, portfolio_data : PortfolioCreate) -> Portfolio:
        stock = self.stock_repo.get_by_id(portfolio_data.stock_id)
        if not stock:
            raise NotFoundException(message="Saham yang dipilih tidak valid")

        new_portfolio = Portfolio(
            user_id=user_id,
            stock_id=portfolio_data.stock_id,
            lots=portfolio_data.lots,
            average_price=portfolio_data.average_price
        )
        return self.portfolio_repo.create(new_portfolio)

    def get_user_portfolio(self, user_id: int) -> list[Portfolio]:
        return self.portfolio_repo.get_by_user_id(user_id)

    def remove_from_portfolio(self, portfolio_id: int, user_id: int) -> None:
        portfolio = self.portfolio_repo.get_by_id(portfolio_id)
        if not portfolio:
            raise NotFoundException(message="Portfolio tidak ditemukan")

        if portfolio.user_id != user_id:
            raise ForbiddenException(message="Anda tidak memiliki akses untuk menghapus portfolio ini")

        self.portfolio_repo.delete(portfolio)