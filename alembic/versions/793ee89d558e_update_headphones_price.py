"""update headphones price

Revision ID: 793ee89d558e
Revises: 3657e26d5901
Create Date: 2025-11-27 15:44:14.863130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '793ee89d558e'
down_revision: Union[str, Sequence[str], None] = '3657e26d5901'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema — update the price of Wireless headphones."""

    op.execute(
        """
        UPDATE product_details
        SET price = 179.99
        WHERE description = 'Wireless headphones with noise cancelling'
          AND product_id = (
                SELECT id FROM product WHERE name = 'Headphones'
          );
        """
    )


def downgrade() -> None:
    """Downgrade schema — revert the updated price back to original."""

    op.execute(
        """
        UPDATE product_details
        SET price = 199.99
        WHERE description = 'Wireless headphones with noise cancelling'
          AND product_id = (
                SELECT id FROM product WHERE name = 'Headphones'
          );
        """
    )