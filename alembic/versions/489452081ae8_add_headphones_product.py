"""add headphones product

Revision ID: 489452081ae8
Revises: f02525822385
Create Date: 2025-11-27 15:35:17.831958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '489452081ae8'
down_revision: Union[str, Sequence[str], None] = 'f02525822385'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema — insert Headphones product and details."""

    # Insert Headphones product
    op.execute(
        """
        INSERT INTO product (name)
        VALUES ('Headphones');
        """
    )

    # Insert product_details for Headphones
    op.execute(
        """
        INSERT INTO product_details (product_id, description, price, in_stock)
        VALUES 
        (
            (SELECT id FROM product WHERE name = 'Headphones'),
            'Wireless headphones with noise cancelling',
            199.99,
            true
        ),
        (
            (SELECT id FROM product WHERE name = 'Headphones'),
            'Wired studio headphones',
            149.99,
            true
        );
        """
    )


def downgrade() -> None:
    """Downgrade schema — remove Headphones product and its details."""

    op.execute(
        """
        DELETE FROM product_details
        WHERE product_id = (
            SELECT id FROM product WHERE name = 'Headphones'
        );
        """
    )

    op.execute(
        """
        DELETE FROM product
        WHERE name = 'Headphones';
        """
    )