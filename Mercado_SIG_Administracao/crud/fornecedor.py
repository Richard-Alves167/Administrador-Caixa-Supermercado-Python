from Common.util import *
from Common.crud.produto import return_produto
from Common.models import Fornecedor, Fornecedor_Produto

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
            print("Fornecedor encontrado: ", fornecedor)
    except Exception as e:
        print("Erro:", e)

def read_fornecedores(session):
    print("Listar fornecedores")
    try:
        fornecedores = return_fornecedores(session)
        for fornecedor in fornecedores:
            print(f"{fornecedores[fornecedor].id_fornecedor} - {fornecedores[fornecedor]}")
    except Exception as e:
        print("Erro:", e)

def insert_fornecedor_produto(session, fornecedor_id):
    try:
        fornecedor = return_fornecedor(session, fornecedor_id)
        if fornecedor:
            produto_id = input_int_positivo("Digite o ID do produto: ")
            produto = return_produto(session, produto_id)
            if produto and produto_id not in [p.id_produto for p in fornecedor.produtos]:
                fornecedor_produto = Fornecedor_Produto(int(fornecedor_id), int(produto_id))
                session.add(fornecedor_produto)
                session.commit()
                print("Fornecedor atualizado com sucesso!")
            else:
                print("Produto não cadastrado ou já vinculado ao fornecedor.")
    except Exception as e:
        print("Erro:", e)

def delete_fornecedor_produto(session, fornecedor_id):
    try:
        fornecedor = return_fornecedor(session, fornecedor_id)
        if fornecedor:
            produto_id = input_int_positivo("Digite o ID do produto: ")
            produto = return_produto(session, produto_id)
            if produto and produto_id in [p.id_produto for p in fornecedor.produtos]:
                session.delete(session.get(Fornecedor_Produto, (fornecedor_id, produto_id)))
                session.commit()
                print("Fornecedor atualizado com sucesso!")
            else:
                print("Produto não cadastrado ou não está vinculado ao fornecedor.")
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