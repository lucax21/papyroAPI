"""create rate table

Revision ID: e2d011e626b6
Revises: ecc9f018970f
Create Date: 2022-07-28 17:43:31.327071

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'e2d011e626b6'
down_revision = 'ecc9f018970f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('rate',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('text', sa.Text(), nullable=True),
                    sa.Column('date', sa.DateTime(), nullable=True),
                    sa.Column('rate', sa.Integer(), nullable=True),
                    sa.Column('likes', sa.Integer(), nullable=True),
                    sa.Column('fk_user', sa.Integer(), nullable=True),
                    sa.Column('fk_book', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['fk_book'], ['book.id'], ),
                    sa.ForeignKeyConstraint(['fk_user'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_rate_id'), 'rate', ['id'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_rate_id'), table_name='rate')
    op.drop_table('rate')
