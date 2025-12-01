from Common.conexao import caminho_arquivo
from Common.models import Produto
from Mercado_SIG_Administracao.web.scraping_produtos import buscar_produtos_site
from sqlalchemy import create_engine
import os
import pandas as pd

def mocki_arquivo_produtos():
    lista_produtos = buscar_produtos_site()
    try:
        arquivo = open("Common/datasets/produtos.csv","w", encoding='utf-8')
        arquivo.write("nome;quantidade;preco;id_desconto;quantidade_min_para_desconto\n")
        for produto in lista_produtos:
            linha = f"{produto}\n"
            arquivo.write(linha)
        print("Arquivo de produtos criado com sucesso!")
    except Exception as e:
        print("Erro ao criar arquivo de produtos:", e)

def deletar_arquivo_produtos():
    if os.path.isfile("Common/datasets/produtos.csv"):
        try:
            os.remove("Common/datasets/produtos.csv")
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
            print("Tabela de Produtos criada com sucesso!")
    except Exception as e:
        print("Erro ao criar tabela:", e)

def resetar_tabela_produto():
    try:
        engine = create_engine("sqlite:///" + caminho_arquivo())
        if engine.dialect.has_table(engine.connect(), "produto"):
            Produto.__table__.drop(engine)
        print("Tabela de Produtos resetada com sucesso!")
    except Exception as e:
        print("Erro ao resetar tabela:", e)

def mocki_produtos(session):
    try:
        produtos_mocki = pd.read_csv("Common/datasets/produtos.csv",sep=";", encoding="utf-8").values.tolist()
        for produto in produtos_mocki:
            produto = Produto(produto[0], int(produto[1]), float(produto[2]), int(produto[3]), int(produto[4]))
            session.add(produto)
        session.commit()
    except Exception as e:
        print("Erro ao inserir produtos mocki:", e)