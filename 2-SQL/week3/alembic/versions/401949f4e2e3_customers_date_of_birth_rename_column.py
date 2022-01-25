""" customers date_of_birth rename column 

Revision ID: 401949f4e2e3
Revises: 95c3ab87fde8
Create Date: 2022-01-19 00:30:33.026859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '401949f4e2e3'
down_revision = '95c3ab87fde8'
branch_labels = None
depends_on = None

def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        RENAME COLUMN date_of_birth TO dob;
        """
    )

def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        RENAME COLUMN dob TO date_of_birth;
        """
    )