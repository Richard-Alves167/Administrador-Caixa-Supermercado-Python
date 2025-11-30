from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import event
import os.path

def caminho_arquivo():
    BANCO = "datasets/mercado.sql"
    DIR = os.path.dirname(os.path.abspath(__file__))
    ARQ = os.path.join(DIR, BANCO)
    return ARQ

engine = create_engine("sqlite:///" + caminho_arquivo())

@event.listens_for(engine, "connect")
def enable_fk(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

def conectar():
    session = None
    try:
        session = sessionmaker(bind = engine)()
    except Exception as ex:
        print(ex)
    return session

def desconectar(session):
    if session:
        session.close()