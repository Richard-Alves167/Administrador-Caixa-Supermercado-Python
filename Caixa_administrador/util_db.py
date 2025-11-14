from sqlalchemy import create_engine
from conexao import conectar, desconectar, caminho_arquivo
from models import *
import os
import pandas as pd
import json

def criar_tabela_produto():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if not engine.dialect.has_table(engine.connect(), "produto"):
            from models import Produto
            Produto.__table__.create(bind=engine)
            print("Tabela criada com sucesso!")
    except Exception as e:
        print("Erro ao criar tabela:", e)

def resetar_tabela_produto():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if engine.dialect.has_table(engine.connect(), "produto"):
            Produto.__table__.drop(engine)
        print("Tabela resetada com sucesso!")
    except Exception as e:
        print("Erro ao resetar tabela:", e)

def mocki_produtos(session):
    produtos_mocki = [
        Produto("Pitaya", 100, 9.99),
        Produto("Uva", 30, 6.99),
        Produto("Melancia", 300, 18.99),
        Produto("Morango", 200, 4.99),
        Produto("Carambola", 0, 23.99)
    ]
    try:
        session.add_all(produtos_mocki)
        session.commit()
    except Exception as e:
        print("Erro ao inserir produtos mocki:", e)

def mocki_arquivo_clientes():
    json_clientes = json.dumps(['Cliente 1','Cliente 2','Cliente 3'])
    try:
        arquivo = open("Caixa_administrador/clientes.json","w")
        arquivo.write(json_clientes)
        arquivo.close()
        print("Arquivo de clientes criado com sucesso!")
    except Exception as e:
        print("Erro ao criar arquivo de clientes:", e)

def deletar_arquivo_clientes():
    if os.path.isfile("Caixa_administrador/clientes.json"):
        try:
            os.remove("Caixa_administrador/clientes.json")
            print("Arquivo de clientes deletado com sucesso!")
        except Exception as e:
            print("Erro ao deletar arquivo de clientes:", e)
    else:
        print("Arquivo de clientes não encontrado.")
