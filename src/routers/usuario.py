from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session

from datetime import date
import re

from typing import List
from src.core.token_provider import check_acess_token, get_confirmation_token
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado
from src.crud.usuario import CrudUsuario
from src.schemas.usuario import Usuario, UsuarioCriar, UsuarioPerfil

from jose import jwt

from src.core.email_provider import Mailer


router = APIRouter()


@router.get("/usuariostest12", response_model=List[Usuario])
async def dados_usuario(session: Session = Depends(get_db)):
    dado = CrudUsuario(session).listar()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado


@router.post("/",status_code=status.HTTP_201_CREATED, response_model=Usuario)
async def cadastrar(usuario: UsuarioCriar, session: Session = Depends(get_db)):
    #verifica campos vazios
    if not usuario.nome:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Nome.")
    elif not usuario.apelido:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Apelido.")
    elif not usuario.senha:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha a Senha.")
    elif not usuario.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o E-mail.")
    elif not usuario.data_nascimento:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha a Data de Nascimento.")


    #verifica senha
    """
    a expressão do regex diz:
    - senha deve ter de 8 a 20 digitos
    - espaços em branco não são permitidos
    """
    result_senha = re.match('^(?=\\S+$).{8,20}$', usuario.senha)
    if not result_senha:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A Senha deve conter no mínimo 8 dígitos e no máximo 20 dígitos.")

    #verifica se é maior de 18 anos
    idade = (date.today() - usuario.data_nascimento)
    result_idade = (idade.days / 365.25)
    if result_idade < 18.0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Você deve ser maior de idade para criar um conta.")

    #verifica se o apelido já está sendo utilizado
    apelido_buscado = CrudUsuario(session).buscar_por_apelido(usuario.apelido)
    if apelido_buscado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse apelido.")
    #verifica se o email já está sendo utilizado
    email_buscado = CrudUsuario(session).buscar_por_email(usuario.email)
    if email_buscado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse email.")
    
 
    #cria o novo usuário
    usuario_criado = CrudUsuario(session).criar_usuario(usuario)

    token_confirmacao = get_confirmation_token(usuario_criado.email, usuario_criado.confirmacao)

    try:
        Mailer.enviar_email_confirmacao(token_confirmacao["token"], usuario_criado.email)
    except ConnectionRefusedError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Email não poderia ser enviado. Por favor, tente de novo."
        )

    return usuario_criado

@router.get("/verificacao/{token}",status_code=status.HTTP_201_CREATED, response_model=Usuario)
def verificar(token: str, session: Session = Depends(get_db)):
    invalid_token_error = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Token")

    # Trying decode token
    try:
        payload = check_acess_token(token)
        # print("##############")
        # print(payload)
        # # print(payload['scope'])
        # print("#############33")
    except jwt.JWSError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Token has Expired")


    #check if the scope is ok
    # if payload['scope'] != 'registration':
    #     raise invalid_token_error
    
    # try to get an user with the id from token
    # user = CrudUsuario(session).buscar_por_email(email=payload['sub'])
    user = CrudUsuario(session).buscar_por_email(email=payload)

    # check if we found an user and if the uid confirmation is the same of the token
    # if not user or (user.confirmacao) != payload['jti']:
    #     raise invalid_token_error
    
    #check if the user is already active
    if user.ativo:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="User already Activated")
    
    # if all it's ok, we update the confirmation and 'ativo' attribute and call the save
    user.confirmacao = None
    user.ativo = True
    CrudUsuario(session).ativar_conta(user)

    return user

@router.get("/conversas", response_model=Usuario)
def conversas(session: Session = Depends(get_db)
            , current_user: Usuario = Depends(obter_usuario_logado)):
    pass

@router.get("/buscarUsuarios{termo}",response_model=List[Usuario])
def buscar_usuario(termo: str,session: Session = Depends(get_db)):
    if not termo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Termo de pesquisa vazio.")

    dado = CrudUsuario(session).buscar_por_nome(termo)
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado

@router.get("/get/{id}",response_model=Usuario)
def buscar_por_id(id: int,session: Session = Depends(get_db)):
    if not id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Termo de pesquisa vazio.")

    dado = CrudUsuario(session).buscar_por_id(id)
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado

@router.get("/meusDados",response_model=Usuario)
def dados_usuarios(session: Session = Depends(get_db),current_user: Usuario = Depends(obter_usuario_logado)):  
    return CrudUsuario(session).buscar_por_id(current_user.id)

#,response_model=UsuarioPerfil
@router.get("/visualizarPerfil/{id}", response_model=UsuarioPerfil)
def dados_perfil(id:int, session: Session = Depends(get_db),current_user: Usuario = Depends(obter_usuario_logado)):  
    return CrudUsuario(session).perfil_usuario(id)


@router.put("/atualizarDados")
def editar_dados(usuario: UsuarioCriar, session: Session = Depends(get_db), current_user: Usuario = Depends(obter_usuario_logado)):
    #verifica campos vazios
    if not usuario.nome:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Nome.")
    elif not usuario.apelido:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Apelido.")
    # elif not usuario.senha:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha a Senha.")
    # elif not usuario.senha_confirmacao:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha a Senha de Confirmação.")
    elif not usuario.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o E-mail.")
    elif not usuario.data_nascimento:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha a Data de Nascimento.")


    if(usuario.senha):
        #verifica senha
        """
        a expressão do regex diz:
        - senha deve ter de 8 a 20 digitos
        - espaços em branco não são permitidos
        """
        result_senha = re.match('^(?=\\S+$).{8,20}$', usuario.senha)
        if not result_senha:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A Senha deve conter no mínimo 8 dígitos e no máximo 20 dígitos.")

    #verifica se é maior de 18 anos
    idade = (date.today() - usuario.data_nascimento)
    result_idade = (idade.days / 365.25)
    if result_idade < 18.0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Você deve ser maior de idade para criar um conta.")

    if not usuario.senha == usuario.senha_confirmacao:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Senhas incompatíveis. Confirme novamente.")

    usuario_db = CrudUsuario(session).buscar_por_id(current_user.id)

    if not usuario.apelido == usuario_db.apelido:     
        #verifica se o apelido já está sendo utilizado
        apelido_buscado = CrudUsuario(session).buscar_por_apelido(usuario.apelido)
        if apelido_buscado:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse apelido.")


    if not usuario.email == usuario_db.email:
        #verifica se o email já está sendo utilizado
        email_buscado = CrudUsuario(session).buscar_por_email(usuario.email)
        if email_buscado:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse email.")
        
        # desabilitar confirmação de conta
        CrudUsuario(session).desabilitar_confirmação(current_user.id)

        token_confirmacao = get_confirmation_token(usuario_db.email, usuario_db.confirmacao)

        try:
            Mailer.enviar_email_confirmacao(token_confirmacao["token"], usuario_db.email)
        except ConnectionRefusedError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Email não poderia ser enviado. Por favor, tente de novo."
            )
   
    return CrudUsuario(session).atualizar_usuario(current_user.id, usuario)

@router.post("/testFOTO")
def test(file: UploadFile):
    

    # SOMENTE UM TESTE



    # contents = file.read()

    print(file.filename)
    print(file.content_type)


    from firebase_admin import credentials, initialize_app, storage

    # import pyrebase
    aa = {
        "type": "service_account",
        "project_id": "ethereal-shape-340121",
        "private_key_id": "7c01291e2904884a0493c3e2fa6015f3909ce18d",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCaeM3jSjZAuJMk\nT3v/adWPIW+ZSSpz9yywcq/cMh2hnzWYExYt5Lw8U+hDByx9Mws0nIkL1gOnzyAi\nmZSxODotb9jnlq5r6pmCcrxJk2AeBDQK855yARFgVtI7+t2qBcwQdOMf/2nM+TgZ\ndKDa9tLh3n0YSG23BbOxqxy8mTfuJES+0cenjqS6Kf9IY2AgNBRZUO33/HhyVEwo\nuR9rcWaeHKmYSK+NmMzgp9Lrgh1MQ5HXJjduXz1H1K7gVcxauJ0dakCn7XZ06rTE\nT7cTTvePEkTYl3hCMUZwL0vH+qb3Z/X3dOxS3yqW2cB9TTme+lujc99Bnp7u2du/\n8VI/x7GrAgMBAAECggEAAyrl5CVkqBPEanD57Z/hoDYUweAJqH0cSu7fH6ayi747\nezlmTkEPSN+h007udkiO5Xz1JLKoOohc5cb1kQ4Xx8ITuZQDxEoUs440wY3txPp4\na57ZReuky+hi+iQdIRUVILjRVGD6Uabs3MtvV6cDZgb7m7X6SRbV1+y6Oq7xM+Ov\nBADQpT6dFxYr0o+srhs7OBWMXTJJfUJ4LFY8v3K4brDSaNdkzmhfW0yXFWUY7pVw\n+9zxaa8DMRGUejE18mWqQuRQLFRNrE3QReuSAuWbe+ZqqkontZjEheZomwHgIRWi\naKHGCcca/ihaHjodL6/ys6fiCOKN+wgFE059SlW/UQKBgQDHtV0zXMUztAtSyXa5\nxZhAyU+ohU/56nZO9879bECFMURMwpbbOJ4t/4NevFIJgEWMGYTjjnvHZ3dgGr/G\ncucPrEyqYPKxh3ChnMUUPLeFuifvB4EBBrgHMTJJqD4vo6Q0aYRH3WyLjAU7tLgl\nUtcryyWtnF/EXyCByjf0ds+g4wKBgQDGAz5l+FbUHZs7A3nCJN1Ql5WUQSCw0oFp\ngxYpolUIhlKY1yEJuopm+s4xpFkj4Uxwds1icblthYsXUY0bYPtbQe73tTnXwVv+\ngUsGWvixO3uCZ80VjqYd6OYjO4/tsZ3L6tKxM41wjfMtfc1CWYKBxLi3eoFh2OTe\neuW4z2VumQKBgAlh7PIHzsACGnIWQvyxWtjYXGS3dq1wJYTKQbBIULOxP9s3XS0J\neO0CTyK5SEVoAFx3qnWicRBKPSKHvzDMnyxuVN/AVEag7Vq6acvsmlavC0dAm//3\nV9gGqK0rOVi1oHZR6sQRlBLuTiSi9e/S94b4MVn5ucoZCgbvADf9CP4vAoGAOcHA\ndaXWTdDE8pW08jgmhddxPekxS+Ja9RfTYxmCjBYCCarWbCwJKriFZF130storHU6\nuzhIyfVl+MtEyXOkXZ4BwicOVCyGVNoJtDTczXV4NTVp0JvnQFoqpqQ8+ywPxucb\nxawv2WDOSbqkIHJTat6isoH9Mzk8qNhYIWv9PiECgYEAgZvSdFOSSqY46l0q8t90\ns2Vad0V2xhYHLzUpDhGlPgbxktJq2pFD1e7df0f+ZwQUUT4xhmc8ekz07QDWF1ID\nFuDlRFMLwKiPeDShW9Bq+oFalmVc66KYMPr1Mz9cl98eyghKXt/AlBOlM/MAHjBJ\nQ33H5Xs5ptg193Pb4YcqGsU=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-hxill@ethereal-shape-340121.iam.gserviceaccount.com",
        "client_id": "113178869994544661187",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-hxill%40ethereal-shape-340121.iam.gserviceaccount.com"
    }
    cred = credentials.Certificate(aa)

    # initialize firebase
    initialize_app(cred,{'storageBucket': 'ethereal-shape-340121.appspot.com'})
    
    fileName = "/home/lucas/Downloads/Kati-Horna.jpeg"

    bucket = storage.bucket()
    blob = bucket.blob(file)

    from uuid import uuid4
    # Create new token
    new_token = uuid4()

    # Create new dictionary with the metadata
    metadata  = {"firebaseStorageDownloadTokens": new_token}

    # Set metadata to blob
    blob.metadata = metadata
    blob.upload_from_filename(file)

    # Opt : if you want to make public access from the URL
    blob.make_public()

    print("your file url", blob.public_url)

    return "KKK rodou"