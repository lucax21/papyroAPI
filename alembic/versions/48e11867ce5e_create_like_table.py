"""create like table

Revision ID: 48e11867ce5e
Revises: fc9362fe9055
Create Date: 2022-07-28 17:45:06.992963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48e11867ce5e'
down_revision = 'fc9362fe9055'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('like',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('fk_comment', sa.Integer(), nullable=True),
                    sa.Column('fk_rate', sa.Integer(), nullable=True),
                    sa.Column('fk_user', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['fk_comment'], ['comment.id'], ),
                    sa.ForeignKeyConstraint(['fk_rate'], ['rate.id'], ),
                    sa.ForeignKeyConstraint(['fk_user'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_like_id'), 'like', ['id'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_like_id'), table_name='like')
    op.drop_table('like')
