from sqlalchemy import create_engine
from common.conexao import caminho_arquivo
from common.models import *
from Mercado_SIG_Administracao.web.scraping_produtos import buscar_produtos_site
import os
import pandas as pd
import json

def mocki_arquivo_produtos():
    lista_produtos = buscar_produtos_site()
    try:
        arquivo = open("common/datasets/produtos.csv","w", encoding='utf-8')
        arquivo.write("nome;quantidade;preco\n")
        for produto in lista_produtos:
            linha = f"{produto}\n"
            arquivo.write(linha)
        print("Arquivo de produtos criado com sucesso!")
    except Exception as e:
        print("Erro ao criar arquivo de produtos:", e)

def deletar_arquivo_produtos():
    if os.path.isfile("common/datasets/produtos.csv"):
        try:
            os.remove("common/datasets/produtos.csv")
            print("Arquivo de produtos deletado com sucesso!")
        except Exception as e:
            print("Erro ao deletar arquivo de proutos:", e)
    else:
        print("Arquivo de produtos não encontrado.")

def criar_tabela_produto():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if not engine.dialect.has_table(engine.connect(), "produto"):
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
    try:
        produtos_mocki = pd.read_csv("common/datasets/produtos.csv",sep=";").values.tolist()
        for produto in produtos_mocki:
            produto = Produto(produto[0], int(produto[1]), float(produto[2]))
            session.add(produto)
        session.commit()
    except Exception as e:
        print("Erro ao inserir produtos mocki:", e)

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
            print("Tabela criada com sucesso!")
    except Exception as e:
        print("Erro ao criar tabela:", e)

def resetar_tabela_cliente():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if engine.dialect.has_table(engine.connect(), "cliente"):
            Cliente.__table__.drop(engine)
        print("Tabela resetada com sucesso!")
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
