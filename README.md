# Papyro API

### AAAAAAAAAAAAAAAAAAa
O projeto está em docker, então a configuração dele realmente é bem fácil é apenas iniciar o projeto com:
```bash
docker-compose up
```

que ele já vai se encarregar de inicializar os containers. Mas para rodar o projeto é apenas fazer:
```bash
docker-compose up
```

Migrations(Básico do básico):

```bash
alembic revision --autogenerate -m "Nova coluna blablabla"
```

```bash
alembic upgrade head
```

