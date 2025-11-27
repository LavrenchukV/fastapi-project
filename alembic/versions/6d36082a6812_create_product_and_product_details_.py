"""create product and product_details tables

Revision ID: 6d36082a6812
Revises: 61f49fb637c8
Create Date: 2025-11-27 14:44:03.589794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d36082a6812'
down_revision: Union[str, Sequence[str], None] = '61f49fb637c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Створюємо таблицю product
    op.create_table(
        'product',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
    )

    # Створюємо таблицю product_details, пов’язану з product
    op.create_table(
        'product_details',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('product_id', sa.Integer(), sa.ForeignKey('product.id', ondelete='CASCADE'), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('price', sa.Numeric(10, 2), nullable=True),
        sa.Column('in_stock', sa.Boolean(), nullable=False, server_default=sa.text('true')),
    )


def downgrade() -> None:
    """Downgrade schema."""
    # При відкаті спочатку видаляємо залежну таблицю
    op.drop_table('product_details')
    op.drop_table('product')