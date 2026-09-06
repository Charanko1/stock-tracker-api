from sqlalchemy import Column, Integer, Float, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from app.database import Base

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id" , ondelete="CASCADE"), nullable=False)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    lots = Column(Integer, nullable=False)
    average_price = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

    user = relationship("User", back_populates="portfolios")
    stock = relationship("Stock", back_populates="portfolios")
