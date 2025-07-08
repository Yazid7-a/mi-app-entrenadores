"""Merge multiple heads

Revision ID: 59c876289e17
Revises: 6a36c7d23283, d586b5277abf
Create Date: 2025-07-08 21:04:35.705874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59c876289e17'
down_revision = ('6a36c7d23283', 'd586b5277abf')
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
