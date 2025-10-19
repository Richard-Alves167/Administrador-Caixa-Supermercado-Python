from util import *
from crud_produtos import *
from datetime import *
from menus import *

def create_atendimento():
    '''
    Cria um novo atendimento.
    Numero do Cliente | Data e Hora | Lista de Produtos Comprados [[ID, Nome, Quantidade, Preço, Quantidade Comprada]]
    '''

    print("Criar atendimento:")
    numero_cliente = 0
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    produtos_comprados = adicionar_carrinho()
    atendimento = [numero_cliente, data, produtos_comprados]
    return atendimento

def adicionar_carrinho():
    lista_produtos = return_produtos()
    produtos_comprados = []
    while(True):
        menu_compra()
        match input_int("Selecione uma opção: "):
            case 1:
                produto_id = input("Digite o ID do produto a ser adicionado: ")
                produto_encontrado = None
                for index, produto in enumerate(lista_produtos):
                    if (produto[0] == produto_id):
                        produto_encontrado = produto
                        quantidade = input_int_positivo("Quantidade: ")
                        if (int(produto[2]) >= quantidade):
                            lista_produtos[index][2] = int(produto[2]) - quantidade
                            preco_total = quantidade * float(produto[3])
                            produto_comprado = [produto[0], produto[1], quantidade, produto[3], preco_total]
                            produtos_comprados.append(produto_comprado)
                            break
                        else:
                            print("Quantidade indisponível no estoque!")
                            break
                if (produto_encontrado == None):
                    print("Erro: produto não cadastrado.")
            case 2:
                break
            case _:
                print("Opção inválida!")
    update_estoque(lista_produtos)
    return produtos_comprados