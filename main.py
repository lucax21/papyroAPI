from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Morto pela mesma alma que tentei salvar."}
