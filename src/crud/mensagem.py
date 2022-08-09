from sqlalchemy.orm import Session


class CrudMensagem():
    def __init__(self, session: Session):
        self.session = session

    # def carregar_conversas(self, id: int):
    # query = self.session.query(models.Mensagem)\
    #     .options(joinedload(models.Mensagem.usuario_destino)).where(models.Mensagem.fk_destino == 31).order_by(models.Mensagem.data_criacao.desc())
    # #.options(joinedload(models.Amigo.usuario_origem)).where(models.Amigo.fk_origem==1)
    # return query.all()
