"""add column date on table friend and like

Revision ID: 07a40d55c19b
Revises: c37fccaae33c
Create Date: 2022-08-16 16:39:41.707755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07a40d55c19b'
down_revision = 'c37fccaae33c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('friend', sa.Column('date', sa.DateTime(), nullable=True))
    op.add_column('like', sa.Column('date', sa.DateTime(), nullable=True))
    op.execute('''
        UPDATE friend SET date = now();
        UPDATE "like" SET date = now();
    ''')

def downgrade():
    op.drop_column('friend', 'date')
    op.drop_column('like', 'date')
