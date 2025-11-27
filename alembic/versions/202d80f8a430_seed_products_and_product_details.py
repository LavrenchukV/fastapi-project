"""seed products and product_details

Revision ID: 202d80f8a430
Revises: 6d36082a6812
Create Date: 2025-11-27 15:19:01.841180

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '202d80f8a430'
down_revision: Union[str, Sequence[str], None] = '6d36082a6812'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema — insert initial products and product_details."""

    # Insert two products
    op.execute(
        """
        INSERT INTO product (name) VALUES
        ('Laptop'),
        ('Smartphone');
        """
    )

    # Insert multiple product_details for Laptop
    op.execute(
        """
        INSERT INTO product_details (product_id, description, price, in_stock)
        VALUES 
        (
            (SELECT id FROM product WHERE name = 'Laptop'),
            'Business laptop 16GB RAM',
            1299.99,
            true
        ),
        (
            (SELECT id FROM product WHERE name = 'Laptop'),
            'Gaming laptop 32GB RAM',
            1899.99,
            true
        );
        """
    )

    # Insert product_details for Smartphone
    op.execute(
        """
        INSERT INTO product_details (product_id, description, price, in_stock)
        VALUES 
        (
            (SELECT id FROM product WHERE name = 'Smartphone'),
            'Smartphone 128GB storage',
            699.99,
            true
        ),
        (
            (SELECT id FROM product WHERE name = 'Smartphone'),
            'Smartphone 256GB storage',
            799.99,
            false
        );
        """
    )


def downgrade() -> None:
    """Downgrade schema — remove initial seeded product data."""

    # Remove only the seeded data (by product name)
    op.execute(
        """
        DELETE FROM product_details
        WHERE product_id IN (
            SELECT id FROM product
            WHERE name IN ('Laptop', 'Smartphone')
        );
        """
    )

    op.execute(
        """
        DELETE FROM product
        WHERE name IN ('Laptop', 'Smartphone');
        """
    )