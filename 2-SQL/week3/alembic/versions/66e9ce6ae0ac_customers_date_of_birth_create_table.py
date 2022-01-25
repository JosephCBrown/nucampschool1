""" customers date_of_birth create table 

Revision ID: 66e9ce6ae0ac
Revises: 401949f4e2e3
Create Date: 2022-01-19 00:32:10.265194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66e9ce6ae0ac'
down_revision = '401949f4e2e3'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE orders(
            id SERIAL PRIMARY KEY,
            dollar_amount_spent NUMERIC,
            customer_id INT NOT NULL,
            CONSTRAINT fk_orders_customers
                FOREIGN KEY (customer_id)
                REFERENCES customers(id)
                ON DELETE CASCADE
        );
        """
    )

def downgrade():
    op.execute(
        """
        DROP TABLE orders;
        """
    )