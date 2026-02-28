"""add foreign-key to posts table

Revision ID: d38a98faa875
Revises: 0b8a275a00d4
Create Date: 2026-02-27 16:09:32.626419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd38a98faa875'
down_revision: Union[str, Sequence[str], None] = '0b8a275a00d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("owner_id", sa.Integer, nullable=False))
    op.create_foreign_key("posts_users_fk",source_table="posts",source_columns=["owner_id"],referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("posts_users_fk",table_name= "posts")
    op.drop_column("posts", "owner_id")
    pass
