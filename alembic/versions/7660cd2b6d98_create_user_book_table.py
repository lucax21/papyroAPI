"""create user_book table

Revision ID: 7660cd2b6d98
Revises: 9dfdfe20a65d
Create Date: 2022-07-28 17:35:56.194436

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '7660cd2b6d98'
down_revision = '9dfdfe20a65d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user_book',
                    sa.Column('fk_book', sa.Integer(), nullable=False),
                    sa.Column('fk_user', sa.Integer(), nullable=False),
                    sa.Column('fk_status', sa.Integer(), nullable=True),
                    sa.Column('date', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['fk_book'], ['book.id'], ),
                    sa.ForeignKeyConstraint(['fk_status'], ['status.id'], ),
                    sa.ForeignKeyConstraint(['fk_user'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('fk_book', 'fk_user')
                    )


def downgrade():
    op.drop_table('user_book')
