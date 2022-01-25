"""add customers date_of_birth

Revision ID: 9f5e2ddd86c0
Revises: d964cbbb9922
Create Date: 2022-01-19 00:12:15.118772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f5e2ddd86c0'
down_revision = 'd964cbbb9922'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )

def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )