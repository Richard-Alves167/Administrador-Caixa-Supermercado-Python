from util import *
from crud_produtos import *
from crud_atendimentos import *
from tabulate import tabulate

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
    print("========== Lista de Atendimentos ==========\n")
    cabecalho = ["Nome", "Idade", "Profissão"]
    print(tabulate(lista_atendimentos, headers=cabecalho))

def atender_cliente():
    atendimento = create_atendimento()
    if (not atendimento[2] == []):
        insert_atendimento(atendimento)
        emitir_nota_fiscal(atendimento)
    else: 
        print("Erro: Atendimento/Carrinho sem produtos...")

def emitir_nota_fiscal(atendimento):
    cliente = atendimento[0]
    data = atendimento[1]
    contador = 1
    total = 0
    produtos = []
    for item in atendimento[2]:
        produtos.append([contador, item[0], item[1], item[2], item[3]])
        total += item[3]
        contador += 1

    print(f"CLiente {cliente}")
    print(f"Data: {data}")
    print()
    cabecalho = ["Item", "Produto", "Quant."," Preço", "Total"]
    print(tabulate(produtos, headers=cabecalho))
    print()
    print(f"Itens: {contador}")
    print(f"Total: {total:.2f}")

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


def emitir_nota_clientes_atendidos(lista_clientes):
    lista_clientes_separados = []
    for cliente in lista_clientes:
        nome_cliente = f"Cliente {cliente[0]}"
        total_cliente = sum([produto[3] for produto in cliente[2]])
        lista_clientes_separados.append([nome_cliente, total_cliente])
    total = sum([cliente[1] for cliente in lista_clientes_separados])

    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    print("Fechamento do caixa")
    print(f"Data: {data}")
    print()
    cabecalho = ["Cliente", "Total"]
    print(tabulate(lista_clientes_separados, headers=cabecalho))
    print()
    print(f"Total: {total:.2f}")

def verificar_produtos_indisponiveis():
    lista_produtos = return_produtos()
    produtos_indisponiveis = [produto for produto in lista_produtos if int(produto[2]) == 0]
    if (not produtos_indisponiveis == []):
        print("Produtos sem estoque:")
        for produto in produtos_indisponiveis:
            print(produto[1])
    else:
        print("Todos os produtos estão com estoque disponível.")


def fechar_caixa():
    lista_clientes = return_atendimentos()
    emitir_nota_clientes_atendidos(lista_clientes)
    lista_produtos = return_estoque_atual()
    update_estoque(lista_produtos)
    verificar_produtos_indisponiveis()
    print("Caixa fechado com sucesso!")