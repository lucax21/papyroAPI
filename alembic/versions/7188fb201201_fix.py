"""fix

Revision ID: 7188fb201201
Revises: 1f12dc06fe1e
Create Date: 2022-07-19 22:52:57.774944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7188fb201201'
down_revision = '1f12dc06fe1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'text',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text(),
               existing_nullable=True)
    op.add_column('genre', sa.Column('description', sa.Text(), nullable=True))
    op.alter_column('rate', 'text',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.Text(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rate', 'text',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
    op.drop_column('genre', 'description')
    op.alter_column('comment', 'text',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
    # ### end Alembic commands ###