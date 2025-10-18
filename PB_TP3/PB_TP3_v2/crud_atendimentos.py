from util import *
from crud_produtos import *
from datetime import *
from menus import *

def create_atendimento():
    '''
    Cria um novo atendimento.
    Numero do Cliente | Data e Hora | Lista de Produtos Comprados [[ID, Nome, Quantidade, Preço, Quantidade Comprada], quantidade]
    '''

    print("Criar atendimento:")
    numero_cliente = 0
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    dic_produtos = return_produtos()
    produtos_comprados = []
    while(True):
        menu_compra()
        match input_int("Selecione uma opção: "):
            case 1:
                produto_id = input("Digite o ID do produto a ser adicionado: ")
                produto_encontrado = dic_produtos.get(produto_id)
                if produto_encontrado:
                        quantidade = input_int_positivo("Quantidade: ")
                        if (int(produto_encontrado[2]) >= quantidade):
                            dic_produtos[produto_encontrado[0]][2] = int(produto_encontrado[2]) - quantidade
                            preco_total = quantidade * float(produto_encontrado[3])
                            produto_comprado = [produto_encontrado[0], produto_encontrado[1], quantidade, produto_encontrado[3], preco_total]
                            produtos_comprados.append(produto_comprado)
                        else:
                            print("Quantidade indisponível no estoque!")
                else:
                    print("Erro: produto não cadastrado.")
            case 2:
                break
            case _:
                print("Opção inválida!")
    update_estoque(dic_produtos)
    atendimento = [numero_cliente, data, produtos_comprados]
    return atendimento