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

Instalar o FastAPI:

```bash
pip install fastapi[all]
```

Depois de dar start na venv e instalar o fastApi na mesma, clone o repositório, acesse o mesmo e rode o comando:

```bash
uvicorn main:app --reload
```
