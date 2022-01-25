""" customers date_of_birth 

Revision ID: 9f78d7b34acd
Revises: 9f5e2ddd86c0
Create Date: 2022-01-19 00:22:35.157963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f78d7b34acd'
down_revision = '9f5e2ddd86c0'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth SET DEFAULT now();
        """
    )

def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        ALTER COLUMN date_of_birth DROP DEFAULT;
        """
    )