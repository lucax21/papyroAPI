"""create book table

Revision ID: 4ac899e0eebb
Revises: fbec8a073a10
Create Date: 2022-07-28 17:28:04.209491

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '4ac899e0eebb'
down_revision = 'fbec8a073a10'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('book',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('identifier', sa.String(length=100), nullable=False),
                    sa.UniqueConstraint('identifier'),
                    sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_book_id'), 'book', ['id'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_book_id'), table_name='book')
    op.drop_table('book')
