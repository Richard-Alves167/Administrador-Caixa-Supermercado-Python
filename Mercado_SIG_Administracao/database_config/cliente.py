from Common.conexao import caminho_arquivo
from Common.models import *
from Mercado_SIG_Administracao.web.scraping_produtos import buscar_produtos_site
from sqlalchemy import create_engine
import os
import pandas as pd
import json

def mocki_arquivo_clientes():
    json_clientes = json.dumps(['Cliente 1','Cliente 2','Cliente 3'])
    try:
        arquivo = open("common/datasets/clientes.json","w")
        arquivo.write(json_clientes)
        arquivo.close()
        print("Arquivo de clientes criado com sucesso!")
    except Exception as e:
        print("Erro ao criar arquivo de clientes:", e)

def deletar_arquivo_clientes():
    if os.path.isfile("common/datasets/clientes.json"):
        try:
            os.remove("common/datasets/clientes.json")
            print("Arquivo de clientes deletado com sucesso!")
        except Exception as e:
            print("Erro ao deletar arquivo de clientes:", e)
    else:
        print("Arquivo de clientes não encontrado.")

def criar_tabela_cliente():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if not engine.dialect.has_table(engine.connect(), "cliente"):
            Cliente.__table__.create(bind=engine)
            print("Tabela de Clientes criada com sucesso!")
    except Exception as e:
        print("Erro ao criar tabela:", e)

def resetar_tabela_cliente():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if engine.dialect.has_table(engine.connect(), "cliente"):
            Cliente.__table__.drop(engine)
        print("Tabela de Clientes resetada com sucesso!")
    except Exception as e:
        print("Erro ao resetar tabela:", e)

def mocki_clientes(session):
    dataframe_clientes = pd.read_json("common/datasets/clientes.json")
    try:
        for cliente in dataframe_clientes[0]:
            id = cliente.split(" ")[1]
            cliente = Cliente(id, cliente)
            session.add(cliente)
        session.commit()
    except Exception as e:
        print("Erro ao inserir clientes mocki:", e)