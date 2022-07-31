"""create friend table

Revision ID: ecc9f018970f
Revises: 540618ec64f1
Create Date: 2022-07-28 17:39:55.816309

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'ecc9f018970f'
down_revision = '540618ec64f1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('friend',
                    sa.Column('pending', sa.Boolean(), nullable=True),
                    sa.Column('ignored', sa.Boolean(), nullable=True),
                    sa.Column('fk_origin', sa.Integer(), nullable=False),
                    sa.Column('fk_destiny', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['fk_destiny'], ['user.id'], ),
                    sa.ForeignKeyConstraint(['fk_origin'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('fk_origin', 'fk_destiny'))


def downgrade():
    op.drop_table('friend')
