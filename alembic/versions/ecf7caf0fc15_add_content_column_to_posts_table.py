"""add content column to posts table

Revision ID: ecf7caf0fc15
Revises: 0425fb0ac189
Create Date: 2026-02-27 14:00:05.804169

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecf7caf0fc15'
down_revision: Union[str, Sequence[str], None] = '0425fb0ac189'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String, nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
    pass
