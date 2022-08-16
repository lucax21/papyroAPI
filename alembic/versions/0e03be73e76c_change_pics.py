"""change pics

Revision ID: 0e03be73e76c
Revises: c37fccaae33c
Create Date: 2022-08-16 21:15:11.696621

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '0e03be73e76c'
down_revision = '07a40d55c19b'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        '''UPDATE "user" SET photo = 'https://i.pinimg.com/736x/67/4f/c5/674fc554838de6abdbf274bdc0ca446c.jpg' where id > 3''')


def downgrade():
    pass
