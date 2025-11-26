from Common.crud.compra import *
from Common.crud.item import *

def salvar_itens_compra(session, compra, atendimento):
    itens = []
    for produto_carrinho in atendimento.carrinho_produtos:
        item = create_item(compra, produto_carrinho)
        itens.append(item)
    for item in itens:
        insert_item(session, item)
    print("Itens da compra salvos com sucesso!")

def salvar_compra(session, atendimento):
    compra = create_compra(atendimento)
    insert_compra(session, compra)
    print("Compra salva com sucesso!")
    salvar_itens_compra(session, compra, atendimento)