"""insert tables friend, user_book and book

Revision ID: eeed11a8f068
Revises: 5722d93529ab
Create Date: 2022-07-24 17:06:53.815074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eeed11a8f068'
down_revision = '5722d93529ab'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('''
        INSERT INTO
            "friend"(pending, ignored, fk_destiny, fk_origin)
        VALUES
             (false,false,1,2),
             (false,false,1,3),
             (false,false,2,1),
             (false,false,3,2)
    ''')
    op.add_column('rate', sa.Column('fk_like', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'rate', 'like', ['fk_like'], ['id'])


def downgrade():
    op.execute('DELETE FROM "friend"')
    op.drop_constraint(None, 'rate', type_='foreignkey')
    op.drop_column('rate', 'fk_like')
