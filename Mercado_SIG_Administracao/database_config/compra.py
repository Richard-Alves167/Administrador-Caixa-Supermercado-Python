from Common.conexao import caminho_arquivo
from Common.models import *
from sqlalchemy import create_engine

def criar_tabela_compra():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if not engine.dialect.has_table(engine.connect(), "compra"):
            Compra.__table__.create(bind=engine)
            print("Tabela de Compras criada com sucesso!")
    except Exception as e:
        print("Erro ao criar tabela:", e)


def resetar_tabela_compra():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if engine.dialect.has_table(engine.connect(), "compra"):
            Compra.__table__.drop(engine)
        print("Tabela de Compras resetada com sucesso!")
    except Exception as e:
        print("Erro ao resetar tabela:", e)