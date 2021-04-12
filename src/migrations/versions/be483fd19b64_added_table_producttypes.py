"""Added table ProductTypes

Revision ID: be483fd19b64
Revises: 28619cbdb4d0
Create Date: 2021-04-10 18:42:30.295981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be483fd19b64'
down_revision = '28619cbdb4d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('code', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_types')
    # ### end Alembic commands ###