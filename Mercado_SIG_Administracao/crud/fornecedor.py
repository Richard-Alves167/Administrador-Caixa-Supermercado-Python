from Common.util import *
from Common.crud.produto import return_produto
from Common.models import Fornecedor

def create_fornecedor():
    '''
    Cria um novo fornecedor.
    ID | Nome
    '''

    print("Criar fornecedor:")
    nome = input("Nome: ")
    fornecedor = Fornecedor(nome)
    print("Fornecedor criado com sucesso!")
    return fornecedor

def insert_fornecedor(session, fornecedor):
    try:
        session.add(fornecedor)
        session.commit()
        print("Fornecedor inserido com sucesso!")
    except Exception as e:
        print("Erro:", e)

def return_fornecedor(session, fornecedor_id):
    fornecedor_encontrado = None
    try:
        fornecedor = session.query(Fornecedor).get(fornecedor_id)
        if fornecedor:
            fornecedor_encontrado = fornecedor
        else:
            print("Erro: fornecedor não cadastrado.")
    except Exception as e:
        print("Erro:", e)
    return fornecedor_encontrado

def return_fornecedores(session):
    fornecedores_dic = {}
    try:
        fornecedores = session.query(Fornecedor).all()
        for fornecedor in fornecedores:
            fornecedores_dic[fornecedor.id_fornecedor] = fornecedor
    except Exception as e:
        print("Erro:", e)
    return fornecedores_dic

def read_fornecedor(session, fornecedor_id):
    try:
        fornecedor = return_fornecedor(session, fornecedor_id)
        if fornecedor:
            visualizar_dataframe_um_dado_tabela(session, "fornecedor", fornecedor_id)
    except Exception as e:
        print("Erro:", e)

def read_fornecedores(session):
    print("Listar fornecedores")
    try:
        visualizar_dataframe_todos_dados_tabela(session, "fornecedor")
    except Exception as e:
        print("Erro:", e)

def delete_fornecedor(session, fornecedor_id):
    try:
        fornecedor = return_fornecedor(session, fornecedor_id)
        if fornecedor:
            session.delete(fornecedor)
            session.commit()
            print("Fornecedor deletado com sucesso!")
    except Exception as e:
        print("Erro:", e)