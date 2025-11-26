from Common.util import *
from Common.crud.produtos import *
from Common.menus import *
from Common.conexao import *
from Mercado_SIG_Administracao.repository.util_db import *

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

def resetar_banco_de_dados(session):
    resetar_estoque(session)
    resetar_clientes(session)
    resetar_compras(session)
    resetar_itens(session)
    resetar_fornecedores(session)

def resetar_estoque(session):
    deletar_arquivo_produtos()
    mocki_arquivo_produtos()
    resetar_tabela_produto()
    criar_tabela_produto()
    mocki_produtos(session)
    print("Estoque resetado com sucesso!")

def resetar_clientes(session):
    deletar_arquivo_clientes()
    mocki_arquivo_clientes()
    resetar_tabela_cliente()
    criar_tabela_cliente()
    mocki_clientes(session)
    print("Clientes resetados com sucesso!")

def resetar_compras(session):
    resetar_tabela_compra()
    criar_tabela_compra()
    
def resetar_itens(session):
    resetar_tabela_iten()
    criar_tabela_iten()

def resetar_fornecedores(session):
    resetar_tabela_fornecedor()
    criar_tabela_fornecedor()
    mocki_fornecedores(session)
    print("Fornecedores resetados com sucesso!")

def acessar_area_administrador(session):
    senha = input("Digite a senha de administrador: ")
    if (senha == "admin123"):
        print("Acesso concedido!")
        selecionar_opcao_administracao(session)
    else:
        print("Senha incorreta!")

def sair_sistema_administrador():
    print("Saindo do sistema operacional de estoque...")

def selecionar_opcao_administracao(session):
    menu_administracao()
    while(True):
        opcao = input_int("\nSelecione uma opção: ")
        match opcao:
            case 0:
                menu_administracao()
            case 1:
                visualizar_produtos(session)
            case 2:
                visualizar_produto(session)
            case 3:
                adicionar_produto(session)
            case 4:
                modificar_produto(session)
            case 5:
                deletar_produto(session)
            case 6:
                resetar_banco_de_dados(session)
            case 7:
                sair_sistema_administrador()
                break
            case _:
                print("Opção inválida!")