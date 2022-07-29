"""create comment table

Revision ID: fc9362fe9055
Revises: e2d011e626b6
Create Date: 2022-07-28 17:44:25.576350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc9362fe9055'
down_revision = 'e2d011e626b6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('comment',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('text', sa.Text(), nullable=True),
                    sa.Column('date', sa.DateTime(), nullable=True),
                    sa.Column('likes', sa.Integer(), nullable=True),
                    sa.Column('fk_user', sa.Integer(), nullable=True),
                    sa.Column('fk_book', sa.Integer(), nullable=True),
                    sa.Column('fk_rate', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['fk_user'], ['user.id'], ),
                    sa.ForeignKeyConstraint(['fk_rate'], ['rate.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_comment_id'), 'comment', ['id'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_comment_id'), table_name='comment')
    op.drop_table('comment')
