from util import *
from crud_produtos import *
from crud_atendimentos import *

def menu_atendimento():
    print('''
    ==============================
    =  Menu de Caixa Atendimento =
    ==============================
    = 1 - Iniciar Atendimento    =
    ------------------------------
    = 2 - Finalizar Atendimentos =
    ==============================
    ''')

def visualizar_atendimentos():
    lista_atendimentos = return_atendimentos()
    for atendimento in lista_atendimentos:
        print(atendimento)

def visualizar_atendimento(atendimento):
    print(atendimento)

def atender_cliente():
    atendimento = create_atendimento()
    visualizar_atendimento(atendimento)
    if (not atendimento[2] == []):
        insert_atendimento(atendimento)
    else: 
        print("Erro: Atendimento/Carrinho sem produtos...")

def abrir_caixa():
    while(True):
        menu_atendimento()
        opcao = input_int("Selecione uma opção: ")
        match opcao:
            case 1:
                atender_cliente()
            case 2:
                fechar_caixa()
                break
            case _:
                print("Opção inválida!")

def fechar_caixa():
    print("Fechando caixa...")
    lista_clientes = return_atendimentos()
    for cliente in lista_clientes:
        print(cliente)
    print("Caixa fechado com sucesso!")