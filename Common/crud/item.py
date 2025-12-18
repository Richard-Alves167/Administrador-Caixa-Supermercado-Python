from Common.util import *
from Common.models import Item
from datetime import *

def create_item(compra, produto_carrinho):
    '''
    Cria um novo item de uma item.
     desconto do produto na hora da compra e quantidade minima para ter desconto na hora da compra.
    ID | ID da compra | ID do produto | quantidade comprada | preço do produto na hora da compra | id do desconto do produto na hora da compra | quantidade minima para ter desconto na hora da compra.
    '''

    item = Item(compra.id_compra, produto_carrinho.id_produto, produto_carrinho.quantidade, produto_carrinho.preco_unitario, produto_carrinho.id_desconto, produto_carrinho.quantidade_min_para_desconto)
    return item

def insert_item(session, item):
    try:
        session.add(item)
        session.commit()
    except Exception as e:
        print("Erro:", e)

def return_item(session, item_id):
    item_encontrado = None
    try:
        item = session.query(Item).get(item_id)
        if item:
            item_encontrado = item
        else:
            print("Erro: item não cadastrado.")
    except Exception as e:
        print("Erro:", e)
    return item_encontrado

def return_itens(session):
    itens_dic = {}
    try:
        itens = session.query(Item).all()
        for item in itens:
            itens_dic[item.id_item] = item
    except Exception as e:
        print("Erro:", e)
    return itens_dic

def read_item(session, item_id):
    try:
        item = return_item(session, item_id)
        if item:
            visualizar_dataframe_um_dado_tabela(session, "item", item_id)
    except Exception as e:
        print("Erro:", e)

def read_itens(session):
    print("Listar itens")
    try:
        visualizar_dataframe_todos_dados_tabela(session, "item")
    except Exception as e:
        print("Erro:", e)