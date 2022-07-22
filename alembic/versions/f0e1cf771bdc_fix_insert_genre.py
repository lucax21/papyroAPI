"""fix insert genre

Revision ID: f0e1cf771bdc
Revises: 8b7cec397250
Create Date: 2022-07-22 19:37:25.614168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0e1cf771bdc'
down_revision = '8b7cec397250'
branch_labels = None
depends_on = ('1f12dc06fe1e', '992c5f113503', '7188fb201201','ee17e3f862d5')

def upgrade():
    op.execute('''
        INSERT INTO
            "genre"(id, name, description)
        VALUES
             (1, 'Romance', 'Aqui você vai encontrar '),
             (2, 'Fantasia', 'Caracterizado por elementos fantásticos, como magia ou sobrenatural.'),
             (3, 'Ficção Científica', 'As histórias normalmente se passam em um futuro distante, na exploração especial e em viagens no tempo e espaço.'),
             (4, 'Horror', 'Esse gênero consiste na passagem de sentimentos de pavor e tensão ao leitor.'),
             (5, 'Policial', 'As histórias que envolvem um crime ou mistério, como o nome indica e que deve ser solucionado pelo protagonista através de pistas.'),
             (6, 'Distopia', 'As distopias imaginam uma sociedade decadente, muitas vezes após um desastre ecológico ou social, enfrentando governos opressores e desastres ambientais.'),
             (7, 'Thriller e Suspense', 'O nome pode até indicar histórias de terror, mas o suspense trabalha exclusivamente em como empregar o medo psicológico e criar um suspense.'),
             (8, 'Jovem Adulto', 'A ficção para jovens adultos, ou YA, tem como público leitores de 12 a 18 anos e reflete nos personagens os desafios únicos da adolescência.'),
             (9, 'Clássicos', 'Consistem principalmente em livros escritos entre os séculos XVI e XVIII.'),
             (10, 'NÃO FICÇÃO', 'São histórias onde há uma descrição ou representação de um assunto que é apresentado como fato, sendo real ou não.')
    ''')

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
    op.execute('DELETE FROM genre WHERE 1=1')
    op.execute('DELETE FROM "user" WHERE 1=1')

