# Papyro API

### Requisitos para rodar o projeto:
- python3.6 ou superior

Comando para criar um ambiente virtual:

```bash
python -m venv papyroAPI
```

Para dar start neste ambiente, basta (isso no linux):

```bash
source papyroAPI/bin/activate
```

Instalar o FastAPI e outras coisas:

```bash
pip install fastapi[all] sqlalchemy alembic "passlib[bcrypt]" "python-jose[cryptography]"
```

Depois de dar start na venv e instalar o fastApi na mesma, clone o repositório, acesse o mesmo e rode o comando:

```bash
uvicorn src.main:app --reload --reload-dir=src
```

Migrations(Básico do básico):

```bash
alembic revison --autogenerate -m "Nova coluna blablabla"
```

```bash
alembic upgrade head
```

