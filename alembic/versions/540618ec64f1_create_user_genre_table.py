"""create user_genre table

Revision ID: 540618ec64f1
Revises: 7660cd2b6d98
Create Date: 2022-07-28 17:38:45.213345

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '540618ec64f1'
down_revision = '7660cd2b6d98'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user_genre',
                    sa.Column('fk_genre', sa.Integer(), nullable=False),
                    sa.Column('fk_user', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['fk_genre'], ['genre.id'], ),
                    sa.ForeignKeyConstraint(['fk_user'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('fk_genre', 'fk_user'))


def downgrade():
    op.drop_table('user_genre')
