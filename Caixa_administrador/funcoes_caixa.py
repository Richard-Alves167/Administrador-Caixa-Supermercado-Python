from util import *
from util_db import *
from crud_produtos import *
from funcoes_atendimento import *
from menus import *

def visualizar_produto():
    produto_id = input("Digite o ID do produto: ")
    read_produto(produto_id)

def visualizar_produtos():
    read_produtos()

def adicionar_produto():
    produto = create_produto()
    insert_produto(produto)

def modificar_produto():
    produto_id = input("Digite o ID do produto a ser modificado: ")
    if (not return_produto(produto_id) == None):
        menu_modificar_produto()
        opcao = input_int("Selecione uma opção: ")
        match opcao:
            case 1:
                update_produto_preco(produto_id)
            case 2:
                update_produto_quantidade(produto_id)
            case _:
                print("Opção inválida!")
    else:
        print("Produto não encontrado")

def deletar_produto():
    produto_id = input("Digite o ID do produto a ser deletado: ")
    delete_produto(produto_id)

def desligar_sistema():
    print("Desligando sistema...")

def selecionar_opcao_caixa():
    while(True):
        opcao = input_int("Selecione uma opção: ")
        match opcao:
            case 0:
                menu_caixa()
            case 1:
                acessar_area_administrador()
            case 2:
                abrir_caixa()
            case 3:
                desligar_sistema()
                break
            case _:
                print("Opção inválida!")

def acessar_area_administrador():
    senha = input("Digite a senha de administrador: ")
    if (senha == "admin123"):
        print("Acesso concedido!")
        print("Entrando no sistema operacional de estoque...")
        selecionar_opcao_administracao()
    else:
        print("Senha incorreta!")

def resetar_estoque():
    resetar_tabela()
    criar_tabela()
    mocki_produtos()
    print("Estoque resetado com sucesso!")

def sair_sistema_administrador():
    print("Saindo do sistema operacional de estoque...")

def selecionar_opcao_administracao():
    menu_administracao()
    while(True):
        opcao = input_int("\nSelecione uma opção: ")
        match opcao:
            case 0:
                menu_administracao()
            case 1:
                visualizar_produtos()
            case 2:
                visualizar_produto()
            case 3:
                adicionar_produto()
            case 4:
                modificar_produto()
            case 5:
                deletar_produto()
            case 6:
                resetar_estoque()
            case 7:
                sair_sistema_administrador()
                break
            case _:
                print("Opção inválida!")

def abrir_sistema_supermercado():
    print("Inicializando sistema...")
    menu_caixa()
    selecionar_opcao_caixa()
    print("Sistema finalizado")