from Common.conexao import caminho_arquivo
from Common.models import Desconto
from sqlalchemy import create_engine
import os
import pandas as pd

def mocki_arquivo_descontos():
    descontos_info = ["bronze,0.05","prata,0.10","ouro,0.20","esmeralda,0.30","rubi,0.40","diamante,0.50"]
    try:
        arquivo = open("Common/datasets/descontos.txt","w", encoding='utf-8')
        for desconto in descontos_info:
            arquivo.write(desconto + "\n")
        arquivo.close()
        print("Arquivo de descontos criado com sucesso!")
    except Exception as e:
        print("Erro ao criar arquivo de descontos:", e)

def deletar_arquivo_descontos():
    if os.path.isfile("Common/datasets/descontos.txt"):
        try:
            os.remove("Common/datasets/descontos.txt")
            print("Arquivo de descontos deletado com sucesso!")
        except Exception as e:
            print("Erro ao deletar arquivo de proutos:", e)
    else:
        print("Arquivo de descontos não encontrado.")

def criar_tabela_desconto():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if not engine.dialect.has_table(engine.connect(), "desconto"):
            Desconto.__table__.create(bind=engine)
            print("Tabela de Descontos criada com sucesso!")
    except Exception as e:
        print("Erro ao criar tabela:", e)

def resetar_tabela_desconto():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if engine.dialect.has_table(engine.connect(), "desconto"):
            Desconto.__table__.drop(engine)
        print("Tabela de Descontos resetada com sucesso!")
    except Exception as e:
        print("Erro ao resetar tabela:", e)

def mocki_descontos(session):
    descontos = ler_arquivo_descontos()
    try:
        for desconto in descontos:
            session.add(desconto)
        session.commit()
    except Exception as e:
        print("Erro ao inserir descontos mocki:", e)

def ler_arquivo_descontos():
    lista_descontos = []
    try:
        arquivo = open("Common/datasets/descontos.txt","r", encoding='utf-8')
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(",")
            tier = dados[0]
            percentual = float(dados[1])
            desconto = Desconto(tier, percentual)
            lista_descontos.append(desconto)
        arquivo.close()
    except Exception as e:
        print("Erro ao ler arquivo de descontos:", e)
    return lista_descontos