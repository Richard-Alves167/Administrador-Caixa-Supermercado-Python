from util import *
from crud_produtos import *
from datetime import *

lista_produtos = return_produtos()
lista_atendimentos = []

def create_atendimento():
    '''
    Cria um novo atendimento.
    Numero do Cliente | Data e Hora | Lista de Produtos Comprados [[ID, Nome, Quantidade, Preço, Quantidade Comprada], quantidade]
    '''

    print("Criar atendimento:")
    numero_cliente = len(lista_atendimentos) + 1
    datetime.now().strftime("%d/%m/%Y %H:%M")
    produtos_comprados = []
    while(True):
        menu_compra()
        match input_int("Selecione uma opção: "):
            case 1:
                produto_comprado = adicionar_produto_carrinho()
                if (not produto_comprado == None):
                    produtos_comprados.append(produto_comprado)
            case 2:
                break
            case _:
                print("Opção inválida!")
    atendimento = [numero_cliente, datetime.now().strftime("%d/%m/%Y %H:%M"), produtos_comprados]
    print(atendimento)
    return atendimento

def insert_atendimento(atendimento):
    lista_atendimentos.append(atendimento)
    print("Atendimento finalizado com sucesso!")

def menu_compra():
    print('''
    ==============================
    =      Menu de Compra        =
    ==============================
    = 1 - Adicionar Produto      =
    ------------------------------
    = 2 - Finalizar Compra       =
    ==============================
    ''')

def adicionar_produto_carrinho():
    produto_id = input("Digite o ID do produto a ser adicionado: ")
    produto_encontrado = None
    for index, produto in enumerate(lista_produtos):
        if (produto[0] == produto_id):
            produto_encontrado = produto
            quantidade = input_int_positivo("Quantidade: ")
            if (int(produto[2]) >= quantidade):
                lista_produtos[index][2] = int(produto[2]) - quantidade
                preco_total = quantidade * float(produto[3])
                return [produto[1], quantidade, produto[3], preco_total]
            else:
                print("Quantidade indisponível no estoque!")
                break
    if (produto_encontrado == None):
        print("Produto não encontrado!")
        return produto_encontrado

def return_atendimentos():
    return lista_atendimentos

def return_estoque_atual():
    return lista_produtos