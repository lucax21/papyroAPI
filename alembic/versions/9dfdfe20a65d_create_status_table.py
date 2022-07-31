"""create status table

Revision ID: 9dfdfe20a65d
Revises: 9ee78e8f848c
Create Date: 2022-07-28 17:34:18.888268

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '9dfdfe20a65d'
down_revision = '9ee78e8f848c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('status',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('status', sa.String(length=100), nullable=True),
                    sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_status_id'), 'status', ['id'], unique=False)

    op.execute('''
        INSERT INTO
            status(id, status)
        VALUES
            (1, 'Lendo'),
            (2, 'Lido'),
            (3, 'Quero Ler')
    ''')


def downgrade():
    op.drop_index(op.f('ix_status_id'), table_name='status')
    op.drop_table('status')
