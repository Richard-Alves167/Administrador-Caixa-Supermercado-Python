from Common.util import *
from Common.menus import *
from Common.conexao import *
from Mercado_SIG_Administracao.repository.util_db import *
from Mercado_SIG_Administracao.service.produto import *
from Mercado_SIG_Administracao.service.cliente import *
from Mercado_SIG_Administracao.service.fornecedor import *

def resetar_banco_de_dados(session):
    resetar_estoque(session)
    resetar_clientes(session)
    resetar_compras(session)
    resetar_itens(session)
    resetar_fornecedores(session)
    resetar_relacionamento_fornecedor_produto(session)

def resetar_estoque(session):
    deletar_arquivo_produtos()
    mocki_arquivo_produtos()
    resetar_tabela_produto()
    criar_tabela_produto()
    mocki_produtos(session)
    print("Estoque resetado com sucesso!\n")

def resetar_clientes(session):
    deletar_arquivo_clientes()
    mocki_arquivo_clientes()
    resetar_tabela_cliente()
    criar_tabela_cliente()
    mocki_clientes(session)
    print("Clientes resetados com sucesso!\n")

def resetar_compras(session):
    resetar_tabela_compra()
    criar_tabela_compra()
    print("Compras resetados com sucesso!\n")
    
def resetar_itens(session):
    resetar_tabela_iten()
    criar_tabela_iten()
    print("Itens resetados com sucesso!\n")

def resetar_fornecedores(session):
    resetar_tabela_fornecedor()
    criar_tabela_fornecedor()
    mocki_fornecedores(session)
    print("Fornecedores resetados com sucesso!\n")

def resetar_relacionamento_fornecedor_produto(session):
    resetar_tabela_fornecedor_produto()
    criar_tabela_fornecedor_produto()
    mocki_fornecedores_produtos(session)
    print("Relacionamento Fornecedor <-> Produto resetados com sucesso!\n")

def acessar_area_administrador(session):
    senha = input("Digite a senha de administrador: ")
    if (senha == "admin123"):
        print("Acesso concedido!")
        selecionar_opcao_administracao(session)
    else:
        print("Senha incorreta!")

def selecionar_opcao_administracao(session):
    menu_administracao()
    while(True):
        opcao = input_int("\nSelecione uma opção: ")
        match opcao:
            case 0:
                menu_administracao()
            case 1:
                selecionar_opcao_administracao_produto(session)
            case 2:
                selecionar_opcao_administracao_cliente(session)
            case 3:
                selecionar_opcao_administracao_fornecedor(session)
            case 4:
                resetar_banco_de_dados(session)
            case 5:
                sair("Saindo do sistema operacional de estoque...")
                break
            case _:
                print("Opção inválida!")

def selecionar_opcao_administracao_produto(session):
    menu_administracao_produto()
    while(True):
        opcao = input_int("\nSelecione uma opção: ")
        match opcao:
            case 0:
                menu_administracao_produto()
            case 1:
                selecionar_opcao_produto_CRUD(session)
            case 2:
                selecionar_opcao_produto_consulta(session)
            case 3:
                sair("Saindo do sistema operacional de estoque...")
                break
            case _:
                print("Opção inválida!")

def selecionar_opcao_produto_CRUD(session):
    menu_produto_CRUD()
    while(True):
        opcao = input_int("\nSelecione uma opção: ")
        match opcao:
            case 0:
                menu_produto_CRUD()
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
                resetar_estoque(session)
                resetar_relacionamento_fornecedor_produto(session)
            case 7:
                sair("Saindo do sistema de CRUD de produtos...")
                break
            case _:
                print("Opção inválida!")

def selecionar_opcao_produto_consulta(session):
    menu_produto_consultas()
    while(True):
        opcao = input_int("\nSelecione uma opção: ")
        match opcao:
            case 0:
                menu_produto_consultas()
            case 1:
                visualizar_produtos_mais_vendidos(session)
            case 2:
                visualizar_produtos_menos_vendidos(session)
            case 3:
                visualizar_produtos_pouco_estoque(session)
            case 4:
                visualizar_produto_fornecedores(session)
            case 5:
                visualizar_produtos_sem_fornecedores(session)
            case 6:
                sair("Saindo do sistema de consultas de produtos...")
                break
            case _:
                print("Opção inválida!")

def selecionar_opcao_administracao_cliente(session):
    menu_administracao_cliente()
    while(True):
        opcao = input_int("\nSelecione uma opção: ")
        match opcao:
            case 0:
                menu_administracao_cliente()
            case 1:
                selecionar_opcao_cliente_CRUD(session)
            case 2:
                selecionar_opcao_cliente_consulta(session)
            case 3:
                sair("Saindo do sistema operacional de cliente...")
                break
            case _:
                print("Opção inválida!")

def selecionar_opcao_cliente_CRUD(session):
    menu_cliente_CRUD()
    while(True):
        opcao = input_int("\nSelecione uma opção: ")
        match opcao:
            case 0:
                menu_cliente_CRUD()
            case 1:
                visualizar_clientes(session)
            case 2:
                visualizar_cliente(session)
            case 3:
                resetar_estoque(session)
            case 4:
                sair("Saindo do sistema de CRUD de clientes...")
                break
            case _:
                print("Opção inválida!")

def selecionar_opcao_cliente_consulta(session):
    menu_cliente_consultas()
    while(True):
        opcao = input_int("\nSelecione uma opção: ")
        match opcao:
            case 0:
                menu_cliente_consultas()
            case 1:
                visualizar_clientes_com_compras(session)
            case 2:
                visualizar_clientes_sem_compras(session)
            case 3:
                visualizar_cliente_compras(session)
            case 4:
                visualizar_cliente_compra(session)
            case 5:
                visualizar_clientes_mais_compras(session)
            case 6:
                visualizar_clientes_mais_gasto(session)
            case 7:
                sair("Saindo do sistema de consultas de clientes...")
                break
            case _:
                print("Opção inválida!")

def selecionar_opcao_administracao_fornecedor(session):
    menu_administracao_fornecedor()
    while(True):
        opcao = input_int("\nSelecione uma opção: ")
        match opcao:
            case 0:
                menu_administracao_fornecedor()
            case 1:
                selecionar_opcao_fornecedor_CRUD(session)
            case 2:
                selecionar_opcao_fornecedor_consulta(session)
            case 3:
                sair("Saindo do sistema operacional de fornecedor...")
                break
            case _:
                print("Opção inválida!")

def selecionar_opcao_fornecedor_CRUD(session):
    menu_fornecedor_CRUD()
    while(True):
        opcao = input_int("\nSelecione uma opção: ")
        match opcao:
            case 0:
                menu_fornecedor_CRUD()
            case 1:
                visualizar_fornecedores(session)
            case 2:
                visualizar_fornecedor(session)
            case 3:
                adicionar_fornecedor(session)
            case 4:
                modificar_fornecedor(session)
            case 5:
                deletar_fornecedor(session)
            case 6:
                resetar_fornecedores(session)
                resetar_relacionamento_fornecedor_produto(session)
            case 7:
                sair("Saindo do sistema de CRUD de fornecedores...")
                break
            case _:
                print("Opção inválida!")

def selecionar_opcao_fornecedor_consulta(session):
    menu_fornecedor_consultas()
    while(True):
        opcao = input_int("\nSelecione uma opção: ")
        match opcao:
            case 0:
                menu_fornecedor_consultas()
            case 1:
                visualizar_fornecedores_com_produtos(session)
            case 2:
                visualizar_fornecedores_sem_produtos(session)
            case 3:
                visualizar_produtos_fornecedor(session)
            case 4:
                sair("Saindo do sistema de consultas de clientes...")
                break
            case _:
                print("Opção inválida!")