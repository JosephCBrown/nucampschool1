""" customers date_of_birth drop constraint 

Revision ID: 4c4393a2ad60
Revises: 66e9ce6ae0ac
Create Date: 2022-01-19 00:36:34.711111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c4393a2ad60'
down_revision = '66e9ce6ae0ac'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE orders
        DROP CONSTRAINT fk_orders_customers;
        """
    )

def downgrade():
    op.execute(
        """
        ALTER TABLE orders
        ADD CONSTRAINT fk_orders_customers
        FOREIGN KEY (customer_id)
        REFERENCES customers(id)
        ON DELETE CASCADE;
        """
    )