"""add user table

Revision ID: 0b8a275a00d4
Revises: ecf7caf0fc15
Create Date: 2026-02-27 14:06:13.822218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b8a275a00d4'
down_revision: Union[str, Sequence[str], None] = 'ecf7caf0fc15'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("email", sa.String, nullable=False, unique=True),
        sa.Column("password", sa.String, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email")
    )

    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
    pass
