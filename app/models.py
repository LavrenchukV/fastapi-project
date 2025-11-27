from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    age = Column(Integer, nullable=True)  # the second migration - I want to add age-column
    hashed_password = Column(String, nullable=True)  # <-- add hashed password