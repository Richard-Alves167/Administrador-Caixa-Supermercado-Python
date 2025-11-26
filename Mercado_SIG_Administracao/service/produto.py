from Common.crud.produtos import *
from Common.menus import *

def visualizar_produto(session):
    produto_id = input("Digite o ID do produto: ")
    read_produto(session, produto_id)

def visualizar_produtos(session):
    read_produtos(session)

def adicionar_produto(session):
    produto = create_produto()
    insert_produto(session, produto)

def modificar_produto(session):
    produto_id = input("Digite o ID do produto a ser modificado: ")
    produto = return_produto(session, produto_id)
    if produto:
        menu_modificar_produto()
        opcao = input_int("Selecione uma opção: ")
        match opcao:
            case 1:
                update_produto_preco(session, produto_id)
            case 2:
                update_produto_quantidade(session, produto_id)
            case _:
                print("Opção inválida!")
    else:
        print("Produto não encontrado")

def deletar_produto(session):
    produto_id = input("Digite o ID do produto a ser deletado: ")
    delete_produto(session, produto_id)