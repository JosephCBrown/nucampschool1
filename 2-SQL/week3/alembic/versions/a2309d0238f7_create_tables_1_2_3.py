""" create tables 1 2 3

Revision ID: a2309d0238f7
Revises: 4c4393a2ad60
Create Date: 2022-01-19 00:39:26.402230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2309d0238f7'
down_revision = '4c4393a2ad60'
branch_labels = None
depends_on = None

def upgrade():
    op.execute(
        """
        CREATE TABLE table1 (id SERIAL PRIMARY KEY);
        CREATE TABLE table2 (id SERIAL PRIMARY KEY);
        CREATE TABLE table3 (id SERIAL PRIMARY KEY);
        """
    )

def downgrade():
    op.execute(
        """
        DROP TABLE table3;
        DROP TABLE table2;
        DROP TABLE table1;
        """
    )