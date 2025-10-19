import os.path
from util import *
from datetime import *
from models import Produto
from conexao import conectar, desconectar

def create_produto():
    '''
    Cria um novo produto.
    ID | Nome | Quantidade | Preço  
    '''

    print("Criar produto:")
    id = datetime.now().strftime("%Y%m%d%H%M%S%f")
    nome = input("Nome: ")
    quantidade = input_int_positivo("Quantidade: ")
    preco = input_float_positivo("Preço: ")
    produto = Produto(id, nome, quantidade, preco)
    print("Produto criado com sucesso!")
    return produto

def insert_produto(produto):
    try:
        session = conectar()
        session.add(produto)
        session.commit()
        print("Produto inserido com sucesso!")
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(session)

def return_produto(produto_id):
    produto_encontrado = None
    try:
        session = conectar()
        produto = session.query(Produto).get(produto_id)
        if produto:
            produto_encontrado = produto
        else:
            print("Erro: produto não cadastrado.")
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(session)
    return produto_encontrado

def return_produtos():
    produtos_dic = {}
    try:
        session = conectar()
        produtos = session.query(Produto).all()
        for produto in produtos:
            produtos_dic[produto.id] = produto
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(session)
    return produtos_dic

def read_produto(produto_id):
    try:
        session = conectar()
        produto = return_produto(produto_id)
        if produto:
            print("Produto encontrado: ", produto)
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(session)

def read_produtos():
    print("Listar produtos")
    try:
        session = conectar()
        produtos = session.query(Produto).all()
        for produto in produtos:
            print(produto)
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(session)

def update_produto_preco(produto_id):
    try:
        session = conectar()
        produto = return_produto(produto_id)
        if produto:
            novo_preco = input_float_positivo("Novo preço: ")
            session.query(Produto).filter(Produto.id == produto_id).update({"preco": novo_preco})
            session.commit()
            print("Produto atualizado com sucesso!")
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(session)

def update_produto_quantidade(produto_id):
    try:
        session = conectar()
        produto = return_produto(produto_id)
        if produto:
            nova_quantidade = input_int_positivo("Nova quantidade no estoque: ")
            session.query(Produto).filter(Produto.id == produto_id).update({"quantidade": nova_quantidade})
            session.commit()
            print("Produto atualizado com sucesso!")
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(session)

def delete_produto(produto_id):
    try:
        session = conectar()
        produto = return_produto(produto_id)
        if produto:
            session.delete(produto)
            session.commit()
            print("Produto deletado com sucesso!")
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(session)

def update_estoque(dic_produtos):
    try:
        session = conectar()
        for index_dic in dic_produtos:
            produto = dic_produtos[index_dic]
            session.query(Produto).filter(Produto.id == produto.id).update({"quantidade": produto.quantidade})
        session.commit()
        print("Estoque atualizado com sucesso!")
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(session)