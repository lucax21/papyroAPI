from sqlalchemy import select, update
from sqlalchemy.orm import Session, joinedload

from src.db.models import models
from typing import List

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
 
        # tentativa 1
        # from fastapi.encoders import jsonable_encoder 
        # generosUsuario_data = jsonable_encoder(generosUsuario)
        # print("#########################################")
        # print(generosUsuario_data)
        
        # db_generosUsuario = models.Usuario(**generosUsuario.dict())
        # # print("333333333333333333333333333")
        # # print(db_generosUsuario)
        # self.session.add(db_generosUsuario)
        # self.session.commit()
        # self.session.refresh(db_generosUsuario)
        # return UsuarioGeneros.from_orm(db_generosUsuario)

        # tentativa 2
        # generosUsuario_data = generosUsuario.dict()
        # generos = generosUsuario_data.pop('generos', None)
        # db_generosUsuario = models.Usuario(**generosUsuario_data)
        # # self.session.add(db_generosUsuario)
        # # self.session.commit()
        # # self.session.refresh(db_generosUsuario)

        # id = db_generosUsuario.id

        # for m in generos:
        #     m['genero'] = id
        #     db_aa = models.Genero(**m)
        #     self.session.add(db_aa)
        #     self.session.commit()
        #     self.session.refresh(db_aa)
        
        # return db_generosUsuario
        
        # # tentativa 3 
        # db_aa = models.Usuario(id=24, generos=generosUsuario.generos)
        # self.session.add(db_aa)
        # self.session.commit()
        # return self.session.refresh(db_aa)
        # pass

        # tentativa 4
        
        for i in generosUsuario:
            id_genero = i.idGenero
            print(id_genero)
            self.session.execute(models.usuario_genero.insert().values(fk_usuario=user_id,fk_genero=id_genero))
            self.session.commit()
        return generosUsuario
