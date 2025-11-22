from common.util import *
from common.crud.produtos import *
from common.menus import *
from common.conexao import *
from Mercado_Caixa.service.caixa import *
from Mercado_SIG_Administracao.service.sistema import *

def abrir_sistema_supermercado():
    print("Inicializando sistema...")
    session = conectar()
    menu_sistema()
    selecionar_opcao_sistema(session)
    desconectar(session)
    print("Sistema finalizado")

def desligar_sistema():
    print("Desligando sistema...")

def selecionar_opcao_sistema(session):
    while(True):
        opcao = input_int("Selecione uma opção: ")
        match opcao:
            case 0:
                menu_sistema()
            case 1:
                acessar_area_administrador(session)
            case 2:
                abrir_caixa(session)
            case 3:
                desligar_sistema()
                break
            case _:
                print("Opção inválida!")