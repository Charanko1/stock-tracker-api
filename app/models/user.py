from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from app.db.base_class import Base, text

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

    portofolios = relationship("Portfolio", back_populates="user", cascade="all, delete-orphan")

    

