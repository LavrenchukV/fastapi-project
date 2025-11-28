from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Numeric,
    func,
)
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    age = Column(Integer, nullable=True)  # the second migration - I want to add age-column
    hashed_password = Column(String, nullable=True)  # add hashed password


class Product(Base):
    __tablename__ = "products"  # check if this matches the table name in your migration

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # зв’язок один-до-багатьох або один-до-одного — як тобі треба
    # relationship: one-to-many or one-to-one, depending on your data structure
    details = relationship("ProductDetails", back_populates="product")


class ProductDetails(Base):
    __tablename__ = "product_details"  # verify that this matches your Alembic migration

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    description = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    in_stock = Column(Boolean, nullable=False, default=True)

    # зворотній зв’язок до Product
    # reverse relationship pointing back to Product
    product = relationship("Product", back_populates="details")