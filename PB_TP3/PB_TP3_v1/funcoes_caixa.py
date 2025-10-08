from util import *
from crud_produtos import *

def menu_caixa():
    print('''
    ==============================
    = Menu do Caixa Supermercado =
    ==============================
    = 0 - Visualizar MENU        =
    ------------------------------
    = 1 - Visualizar Produtos    =
    ------------------------------
    = 2 - Visualizar Um Produto  =
    ------------------------------
    = 3 - Adicionar Produto      =
    ------------------------------
    = 4 - Modificar Produto      =
    ------------------------------
    = 5 - Deletar Produto        =
    ------------------------------
    = 6 - Iniciar Atendimento    =
    ------------------------------
    = 7 - Fechar Caixa           =
    ==============================
    ''')

def fechar_caixa():
    print("Desligando sistema...")

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
        print('''
        ==============================
        =     Menu de Modificação    =
        ==============================
        = 1 - Modificar Preço        =
        ------------------------------
        = 2 - Modificar Quantidade   =
        ==============================
        ''')
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

def atender_cliente():
    print("Iniciando atendimento...")


def selecionar_opcao():
    while(True):
        opcao = input_int("Selecione uma opção: ")
        match opcao:
            case 0:
                menu_caixa()
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
                atender_cliente()
            case 7:
                fechar_caixa()
                break
            case _:
                print("Opção inválida!")

def abrir_caixa():
    print("Inicializando sistema...")
    menu_caixa()
    selecionar_opcao()
    print("Sistema finalizado")