"""create user table

Revision ID: 9ee78e8f848c
Revises: 4ac899e0eebb
Create Date: 2022-07-28 17:31:30.367500

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = '9ee78e8f848c'
down_revision = '4ac899e0eebb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=True),
                    sa.Column('name', sa.String(length=255), nullable=True),
                    sa.Column('nickname', sa.String(length=30), nullable=True),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('password', sa.String(length=256), nullable=True),
                    sa.Column('birthday', sa.DateTime(), nullable=True),
                    sa.Column('photo', sa.String(length=255), nullable=True),
                    sa.Column('active', sa.Boolean(), nullable=True),
                    sa.Column('confirmation', postgresql.UUID(as_uuid=True), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
