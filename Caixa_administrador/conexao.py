import os.path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

def caminho_arquivo():
    BANCO = "./mercado.sql"
    DIR = os.path.dirname(os.path.abspath(__file__))
    ARQ = os.path.join(DIR, BANCO)
    return ARQ

def conectar():
    session = None
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        session = sessionmaker(bind = engine)()

    except Exception as ex:
        print(ex)
    return session

def desconectar(session):
    if session:
        session.close()