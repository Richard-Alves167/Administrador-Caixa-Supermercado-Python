from util import *
from crud_produtos import *
from datetime import *
from menus import *

def create_atendimento(session):
    '''
    Cria um novo atendimento.
    Numero do Cliente | Data e Hora | Lista de Produtos Comprados [[ID, Nome, Quantidade, Preço, Quantidade Comprada]]
    '''

    print("Criar atendimento:")
    numero_cliente = 0
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    produtos_comprados = adicionar_carrinho(session)
    atendimento = [numero_cliente, data, produtos_comprados]
    return atendimento

def adicionar_carrinho(session):
    dic_produtos = return_produtos(session)
    produtos_comprados = []
    while(True):
        menu_compra()
        match input_int("Selecione uma opção: "):
            case 1:
                produto_id = input("Digite o ID do produto a ser adicionado: ")
                produto_encontrado = dic_produtos.get(produto_id)
                if produto_encontrado:
                        quantidade = input_int_positivo("Quantidade: ")
                        if (int(produto_encontrado.quantidade) >= quantidade):
                            dic_produtos[produto_encontrado.id].quantidade = int(produto_encontrado.quantidade) - quantidade
                            preco_total = quantidade * float(produto_encontrado.preco)
                            produto_comprado = [produto_encontrado.id ,produto_encontrado.nome, quantidade, produto_encontrado.preco, preco_total]
                            produtos_comprados.append(produto_comprado)
                        else:
                            print("Quantidade indisponível no estoque!")
                else:
                    print("Erro: produto não cadastrado.")
            case 2:
                break
            case _:
                print("Opção inválida!")
    update_estoque(session, dic_produtos)
    return produtos_comprados