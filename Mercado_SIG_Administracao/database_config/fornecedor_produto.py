from Common.conexao import caminho_arquivo
from Common.models import Fornecedor_Produto
from sqlalchemy import create_engine
import pandas as pd

def criar_tabela_fornecedor_produto():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if not engine.dialect.has_table(engine.connect(), "fornecedor_produto"):
            Fornecedor_Produto.__table__.create(bind=engine)
            print("Tabela de relacionamento Fornecedor e Produto criada com sucesso!")
    except Exception as e:
        print("Erro ao criar tabela:", e)
   
def resetar_tabela_fornecedor_produto():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if engine.dialect.has_table(engine.connect(), "fornecedor_produto"):
            Fornecedor_Produto.__table__.drop(engine)
        print("Tabela de relacionamento Fornecedor e Produto resetada com sucesso!")
    except Exception as e:
        print("Erro ao resetar tabela:", e)

def mocki_fornecedores_produtos(session):
    try:
        produtos_fornecedores_mocki = pd.read_excel("common/datasets/fornecedores.xlsx", sheet_name="produtos-fornecedores")
        for _, produto_fornecedor in produtos_fornecedores_mocki.iterrows():
            fornecedor_produto = Fornecedor_Produto(int(produto_fornecedor['id_fornecedor']), int(produto_fornecedor['id_produto']))
            session.add(fornecedor_produto)
        session.commit()
    except Exception as e:
        print("Erro ao inserir relacionamento Fornecedor e Produto mocki:", e)