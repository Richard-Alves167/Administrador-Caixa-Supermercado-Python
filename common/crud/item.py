from Common.util import *
from Common.models import Item
from datetime import *

def create_item(compra, produto_carrinho):
    '''
    Cria um novo item de uma item.
    ID | ID da compra | ID do produto | quantidade comprada | preço do produto na hora da compra.
    '''

    item = Item(compra.id_compra, produto_carrinho[0], produto_carrinho[2], produto_carrinho[3])
    return item

def insert_item(session, item):
    try:
        session.add(item)
        session.commit()
        print("Item inserido com sucesso!")
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
            print("Item encontrada: ", item)
    except Exception as e:
        print("Erro:", e)

def read_itens(session):
    print("Listar itens")
    try:
        itens = return_itens(session)
        for item in itens:
            print(f"{itens[item].item} - {itens[item]}")
    except Exception as e:
        print("Erro:", e)