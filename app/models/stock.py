from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True)
    ticker = Column(String, index=True)
    company_name = Column(String)
    sector = Column(String)

    portofolios = relationship("Portofolio", back_populates="stock")
    