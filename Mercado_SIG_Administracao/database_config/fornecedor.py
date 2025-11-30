from Common.conexao import caminho_arquivo
from Common.models import *
from sqlalchemy import create_engine
import pandas as pd

def criar_tabela_fornecedor():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if not engine.dialect.has_table(engine.connect(), "fornecedor"):
            Fornecedor.__table__.create(bind=engine)
            print("Tabela de Fornecedores criada com sucesso!")
    except Exception as e:
        print("Erro ao criar tabela:", e)
   
def resetar_tabela_fornecedor():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if engine.dialect.has_table(engine.connect(), "fornecedor"):
            Fornecedor.__table__.drop(engine)
        print("Tabela de Fornecedores resetada com sucesso!")
    except Exception as e:
        print("Erro ao resetar tabela:", e)

def mocki_fornecedores(session):
    try:
        fornecedores_mocki = pd.read_excel("common/datasets/fornecedores.xlsx", sheet_name="fornecedores")
        for _, fornecedor in fornecedores_mocki.iterrows():
            fornecedor = Fornecedor(fornecedor['nome'])
            session.add(fornecedor)
        session.commit()
    except Exception as e:
        print("Erro ao inserir fornecedores mocki:", e)