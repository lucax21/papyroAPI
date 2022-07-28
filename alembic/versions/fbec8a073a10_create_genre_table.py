"""create genre table

Revision ID: fbec8a073a10
Revises: 
Create Date: 2022-07-28 17:20:56.540422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbec8a073a10'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('genre', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=True),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.PrimaryKeyConstraint('id'))
    op.create_index(op.f('ix_genre_id'), 'genre', ['id'], unique=False)

    op.execute('''
            INSERT INTO
                "genre"(id, name, description)
            VALUES
                 (1, 'Romance', 'Aqui você vai encontrar histórias de amor e românticas'),
                 (2, 'Fantasy', 'Caracterizado por elementos fantásticos, como magia ou sobrenatural.'),
                 (3, 'Science Fiction', 'As histórias normalmente se passam em um futuro distante, na exploração especial e em viagens no tempo e espaço.'),
                 (4, 'Horror', 'Esse gênero consiste na passagem de sentimentos de pavor e tensão ao leitor.'),
                 (5, 'Mystery and detective', 'As histórias que envolvem um crime ou mistério, como o nome indica e que deve ser solucionado pelo protagonista através de pistas.'),
                 (6, 'Distopia', 'As distopias imaginam uma sociedade decadente, muitas vezes após um desastre ecológico ou social, enfrentando governos opressores e desastres ambientais.'),
                 (7, 'Thriller', 'O nome pode até indicar histórias de terror, mas o suspense trabalha exclusivamente em como empregar o medo psicológico e criar um suspense.'),
                 (8, 'Young Adult', 'A ficção para jovens adultos, ou YA, tem como público leitores de 12 a 18 anos e reflete nos personagens os desafios únicos da adolescência.'),
                 (9, 'Literature', 'Consistem principalmente em livros escritos entre os séculos XVI e XVIII.'),
                 (10, 'Nonfiction', 'São histórias onde há uma descrição ou representação de um assunto que é apresentado como fato, sendo real ou não.')
        ''')


def downgrade():
    op.drop_index(op.f('ix_genre_id'), table_name='genre')
    op.drop_table('genre')

