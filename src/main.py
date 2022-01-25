from fastapi import FastAPI
from src.routers import usuario

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Morto pela mesma alma que tentei salvar."}

app.include_router(usuario.router)
