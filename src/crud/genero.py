from sqlalchemy import select, update
from sqlalchemy.orm import Session, joinedload

from src.db.models import models
from typing import List

from fastapi import HTTPException, status

from src.schemas.usuario import UsuarioGeneros
from src.schemas.genero import GeneroUsuarioCriar

class CrudGenero():
    def __init__(self, session: Session):
        self.session = session

    def listar_generos(self) -> List[models.Genero]:
        return self.session.query(models.Genero).all()
        

    def listar_generos_usuario(self, user_id) -> UsuarioGeneros:
       
        dado = self.session.query(models.Usuario).options(joinedload(models.Usuario.generos)).where(models.Usuario.id == user_id).one()
        # return UsuarioGeneros.from_orm(dado)
        return dado


    def salvar_generos_usuario(self, generosUsuario: List[GeneroUsuarioCriar], user_id):
 
        try:
            for i in generosUsuario:
                id_genero = i.idGenero
                print(id_genero)
                self.session.execute(models.usuario_genero.insert().values(fk_usuario=user_id,fk_genero=id_genero))
                self.session.commit()
            return generosUsuario
        except Exception as error:
                self.session.rollback()
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
