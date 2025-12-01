from Common.util import *
from Common.models import Produto
from Common.log import *
from datetime import *

def create_produto():
    '''
    Cria um novo produto.
    ID | Nome | Quantidade | Preço | ID do desconto | Quantidade mínima para desconto. 
    '''

    print("Criar produto:")
    nome = input("Nome: ")
    quantidade = input_int_positivo("Quantidade: ")
    preco = input_float_positivo("Preço: ")
    id_desconto = input("ID do desconto (pressione enter para nenhum): ")
    quantidade_min_para_desconto = None
    if id_desconto == "":
        id_desconto = None
    else:
        quantidade_min_para_desconto = input_int_positivo("Quantidade mínima para desconto: ")
    produto = Produto(nome, quantidade, preco, id_desconto, quantidade_min_para_desconto)
    print("Produto criado com sucesso!")
    return produto

def insert_produto(session, produto):
    try:
        session.add(produto)
        session.commit()
        print("Produto inserido com sucesso!")
    except Exception as e:
        print("Erro:", e)

def return_produto(session, produto_id):
    produto_encontrado = None
    try:
        produto = session.query(Produto).get(produto_id)
        if produto:
            produto_encontrado = produto
        else:
            print("Erro: produto não cadastrado.")
    except Exception as e:
        print("Erro:", e)
    return produto_encontrado

def return_produtos(session):
    produtos_dic = {}
    try:
        produtos = session.query(Produto).all()
        for produto in produtos:
            produtos_dic[produto.id_produto] = produto
    except Exception as e:
        print("Erro:", e)
    return produtos_dic

def read_produto(session, produto_id):
    try:
        produto = return_produto(session, produto_id)
        if produto:
            print("Produto encontrado: ", produto)
    except Exception as e:
        print("Erro:", e)

def read_produtos(session):
    print("Listar produtos")
    try:
        produtos = return_produtos(session)
        for produto in produtos:
            print(f"{produtos[produto].id_produto} - {produtos[produto]}")
    except Exception as e:
        print("Erro:", e)

def update_produto_preco(session, produto_id):
    try:
        produto = return_produto(session, produto_id)
        if produto:
            antigo_preco = produto.preco
            novo_preco = input_float_positivo("Novo preço: ")
            session.query(Produto).filter(Produto.id_produto == produto_id).update({"preco": novo_preco})
            session.commit()
            print("Produto atualizado com sucesso!")
            criar_log_atualizacao_preco(produto.id_produto, produto.nome, antigo_preco, novo_preco)
    except Exception as e:
        print("Erro:", e)

def update_produto_quantidade(session, produto_id):
    try:
        produto = return_produto(session, produto_id)
        if produto:
            nova_quantidade = input_int_positivo("Nova quantidade no estoque: ")
            session.query(Produto).filter(Produto.id_produto == produto_id).update({"quantidade": nova_quantidade})
            session.commit()
            print("Produto atualizado com sucesso!")
    except Exception as e:
        print("Erro:", e)

def delete_produto(session, produto_id):
    try:
        produto = return_produto(session, produto_id)
        if produto:
            session.delete(produto)
            session.commit()
            print("Produto deletado com sucesso!")
    except Exception as e:
        print("Erro:", e)

def update_estoque(session, carrinho_produtos):
    try:
        for item in carrinho_produtos:
            produto = session.query(Produto).get(item[0])
            produto.quantidade - item[2]
        session.commit()
        print("Estoque atualizado com sucesso!")
    except Exception as e:
        print("Erro:", e)