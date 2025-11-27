"""delete one headphone detail

Revision ID: 3657e26d5901
Revises: 489452081ae8
Create Date: 2025-11-27 15:40:57.605558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3657e26d5901'
down_revision: Union[str, Sequence[str], None] = '489452081ae8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema — delete one specific product_details entry."""

    # Delete ONLY the 'Wired studio headphones' detail
    op.execute(
        """
        DELETE FROM product_details
        WHERE description = 'Wired studio headphones'
        AND product_id = (
            SELECT id FROM product WHERE name = 'Headphones'
        );
        """
    )


def downgrade() -> None:
    """Downgrade schema — restore the deleted product_details entry."""

    op.execute(
        """
        INSERT INTO product_details (product_id, description, price, in_stock)
        VALUES (
            (SELECT id FROM product WHERE name = 'Headphones'),
            'Wired studio headphones',
            149.99,
            true
        );
        """
    )