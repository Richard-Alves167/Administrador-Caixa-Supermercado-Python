from sqlalchemy import create_engine
from conexao import conectar, desconectar, caminho_arquivo
from models import Produto

def criar_tabela():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if not engine.dialect.has_table(engine.connect(), "produto"):
            from models import Produto
            Produto.__table__.create(bind=engine)
            print("Tabela criada com sucesso!")
    except Exception as e:
        print("Erro ao criar tabela:", e)

def resetar_tabela():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if engine.dialect.has_table(engine.connect(), "produto"):
            Produto.__table__.drop(engine)
        print("Tabela resetada com sucesso!")
    except Exception as e:
        print("Erro ao resetar tabela:", e)

def mocki_produtos(session):
    produtos_mocki = [
        Produto(1, "Pitaya", 100, 9.99),
        Produto(2, "Uva", 30, 6.99),
        Produto(3, "Melancia", 300, 18.99),
        Produto(4, "Morango", 200, 4.99),
        Produto(5, "Carambola", 0, 23.99)
    ]
    try:
        session.add_all(produtos_mocki)
        session.commit()
    except Exception as e:
        print("Erro ao inserir produtos mocki:", e)