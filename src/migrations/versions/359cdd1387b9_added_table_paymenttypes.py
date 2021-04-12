"""Added table PaymentTypes

Revision ID: 359cdd1387b9
Revises: fd66f0988356
Create Date: 2021-04-10 19:09:43.950165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '359cdd1387b9'
down_revision = 'fd66f0988356'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment_methods',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('code', sa.Integer(), autoincrement=True, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment_methods')
    # ### end Alembic commands ###