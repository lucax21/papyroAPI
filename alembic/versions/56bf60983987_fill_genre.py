"""fill genre

Revision ID: 56bf60983987
Revises: 7188fb201201
Create Date: 2022-07-19 21:21:11.321573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56bf60983987'
down_revision = '7188fb201201'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('''
        INSERT INTO
            genre(id, name, description)
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


def downgrade():
    op.execute('DELETE FROM genre WHERE 1=1')

