"""add coluna ativo e confirmacao na tb usuario

Revision ID: 0a3d3fb6ce08
Revises: 423eaa7b3d0e
Create Date: 2022-02-19 18:10:19.374565

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0a3d3fb6ce08'
down_revision = '423eaa7b3d0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('ativo', sa.Boolean(), nullable=True))
    op.add_column('usuario', sa.Column('confirmacao', postgresql.UUID(as_uuid=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'confirmacao')
    op.drop_column('usuario', 'ativo')
    # ### end Alembic commands ###