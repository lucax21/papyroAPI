"""add column pin and date_pin on table user

Revision ID: df0916ccb150
Revises: 07a40d55c19b
Create Date: 2022-08-25 22:44:44.978184

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'df0916ccb150'
down_revision = '07a40d55c19b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('code_otp', sa.String(length=6), nullable=True))
    op.add_column('user', sa.Column('code_otp_time', sa.DateTime(), nullable=True))
    op.drop_column('user', 'active')
    op.drop_column('user', 'confirmation')
    op.drop_column('user', 'birthday')
    op.execute(
        '''UPDATE "user" SET photo = 'https://i.pinimg.com/736x/67/4f/c5/674fc554838de6abdbf274bdc0ca446c.jpg' where id > 3''')

def downgrade():
    op.add_column('user', sa.Column('birthday', sa.Date(), nullable=True))
    op.add_column('user', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('confirmation', postgresql.UUID(as_uuid=True), nullable=True))
    op.drop_column('user', 'code_otp')
    op.drop_column('user', 'code_otp_time')
