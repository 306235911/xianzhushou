"""initial migration

Revision ID: 49f87170801f
Revises: 3fefc0faac3d
Create Date: 2016-09-03 10:58:00.570000

"""

# revision identifiers, used by Alembic.
revision = '49f87170801f'
down_revision = '3fefc0faac3d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('buy', sa.String(length=10), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'buy')
    ### end Alembic commands ###
