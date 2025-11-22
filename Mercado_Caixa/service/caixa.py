from common.util import *
from common.crud.produtos import *
from common.menus import *
from common.conexao import *
from Mercado_SIG_Administracao.repository.util_db import *
from Mercado_Caixa.service.atendimento import *

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

def desligar_sistema():
    print("Desligando sistema...")

def selecionar_opcao_caixa(session):
    while(True):
        opcao = input_int("Selecione uma opção: ")
        match opcao:
            case 0:
                menu_caixa()
            case 1:
                acessar_area_administrador(session)
            case 2:
                abrir_caixa(session)
            case 3:
                desligar_sistema()
                break
            case _:
                print("Opção inválida!")

def acessar_area_administrador(session):
    senha = input("Digite a senha de administrador: ")
    if (senha == "admin123"):
        print("Acesso concedido!")
        print("Entrando no sistema operacional de estoque...")
        selecionar_opcao_administracao(session)
    else:
        print("Senha incorreta!")

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
                resetar_estoque(session)
            case 7:
                resetar_clientes(session)
            case 8:
                sair_sistema_administrador()
                break
            case _:
                print("Opção inválida!")

def abrir_sistema_supermercado():
    print("Inicializando sistema...")
    session = conectar()
    menu_caixa()
    selecionar_opcao_caixa(session)
    desconectar(session)
    print("Sistema finalizado")