""" customers date_of_birth not null 

Revision ID: 95c3ab87fde8
Revises: 9f78d7b34acd
Create Date: 2022-01-19 00:29:33.442450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95c3ab87fde8'
down_revision = '9f78d7b34acd'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth SET NOT NULL;
        """
    )

def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth DROP NOT NULL;
        """
    )