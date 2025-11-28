from Mercado_SIG_Administracao.crud.fornecedor import *
from Common.menus import *

def visualizar_fornecedor(session):
    fornecedor_id = input("Digite o ID do fornecedor: ")
    read_fornecedor(session, fornecedor_id)

def visualizar_fornecedores(session):
    read_fornecedores(session)

def adicionar_fornecedor(session):
    fornecedor = create_fornecedor()
    insert_fornecedor(session, fornecedor)

def modificar_fornecedor(session):
    fornecedor_id = input("Digite o ID do fornecedor a ser modificado: ")
    fornecedor = return_fornecedor(session, fornecedor_id)
    if fornecedor:
        print("Fornecedor encontrado:", fornecedor.nome)
        menu_modificar_fornecedor()
        opcao = input_int("Selecione uma opção: ")
        match opcao:
            case 1:
                insert_fornecedor_produto(session, fornecedor_id)
            case 2:
                delete_fornecedor_produto(session, fornecedor_id)
            case 3:
                sair("Saindo da opção de modificação de fornecedor...")
            case _:
                print("Opção inválida!")
    else:
        print("fornecedor não encontrado")

def deletar_fornecedor(session):
    fornecedor_id = input("Digite o ID do fornecedor a ser deletado: ")
    delete_fornecedor(session, fornecedor_id)