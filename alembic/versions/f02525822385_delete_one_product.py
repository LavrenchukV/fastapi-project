"""delete one product

Revision ID: f02525822385
Revises: 202d80f8a430
Create Date: 2025-11-27 15:21:07.273820

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f02525822385'
down_revision: Union[str, Sequence[str], None] = '202d80f8a430'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema — delete one product and its details."""

    # Optionally: demonstrate read/update before delete
    # (not required, but can be mentioned)
    op.execute("SELECT * FROM product;")
    op.execute("SELECT * FROM product_details;")

    # Example UPDATE: change price of one Smartphone variant
    op.execute(
        """
        UPDATE product_details
        SET price = 749.99
        WHERE product_id = (SELECT id FROM product WHERE name = 'Smartphone')
          AND description = 'Smartphone 128GB storage';
        """
    )

    # DELETE: remove Smartphone (CASCADE will delete its product_details)
    op.execute(
        """
        DELETE FROM product
        WHERE name = 'Smartphone';
        """
    )


def downgrade() -> None:
    """Downgrade schema — restore deleted product and its details."""

    # Re-insert Smartphone product
    op.execute(
        """
        INSERT INTO product (name)
        VALUES ('Smartphone');
        """
    )

    # Re-insert Smartphone details
    op.execute(
        """
        INSERT INTO product_details (product_id, description, price, in_stock)
        VALUES 
        (
            (SELECT id FROM product WHERE name = 'Smartphone'),
            'Smartphone 128GB storage',
            749.99,
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