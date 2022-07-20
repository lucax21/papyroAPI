"""fill user

Revision ID: c320c38372b8
Revises: 56bf60983987
Create Date: 2022-07-19 21:51:56.602478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c320c38372b8'
down_revision = '56bf60983987'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('''
    INSERT INTO
        "user"(id, email, name, nickname, description, password, birthday, photo, active, confirmation)
    VALUES
        (1,
        'wgiacomin@pm.me',
        'Wanderson Giacomin',
        'Wanderson',
        'Aficionado em Fantasia',
        '$2b$12$oVdwTmriZq4StlbbFXIrlO9WxXbwg5TRnv6xIiRBh7OQfdnTb12nu',
        '1993-08-24',
        'https://images.gr-assets.com/users/1616356479p8/96644171.jpg',
        true,
        '04d0f619-261b-4203-848c-ed24cf5db170'),
        (2,
         'lucax.oliveira96@gmail.com',
         'Lucas Oliveira',
         'Lucas',
         'Autor dos mais diversos romances',
         '$2b$12$oVdwTmriZq4StlbbFXIrlO9WxXbwg5TRnv6xIiRBh7OQfdnTb12nu',
         '1994-01-10',
         'https://images.gr-assets.com/photos/1610930279p8/3981752.jpg',
         true,
         '88d1c470-6bf1-431a-9297-3a128762b8af'),
        (3,
         'anacaroldolata@gmail.com',
         'Ana Dolata',
         'Ana',
         'Romance, amo romances!',
         '$2b$12$oVdwTmriZq4StlbbFXIrlO9WxXbwg5TRnv6xIiRBh7OQfdnTb12nu',
         '1996-02-28',
         'https://images.gr-assets.com/users/1611553147p8/50690704.jpg',
         true,
         '478fdae1-70d8-4b4c-a45f-954cdcc4ebf0')
    ''')


def downgrade():
    op.execute('DELETE FROM user WHERE 1=1')
