from Common.util import *
from Common.crud.produtos import *
from Common.models import Atendimento
from Common.menus import *
from Mercado_Caixa.data.tabela import agrupar_itens_carrinho
from datetime import *

def create_atendimento(session, id_cliente):
    '''
    Cria um novo atendimento.
    Numero do Cliente | Data e Hora | Lista de Produtos Comprados [[ID, Nome, Quantidade, Preço, Quantidade Comprada]]
    '''

    print("Criar atendimento:")
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    produtos_comprados = adicionar_carrinho(session)
    atendimento = Atendimento(id_cliente, data, produtos_comprados)
    return atendimento

def adicionar_carrinho(session):
    dic_produtos = return_produtos(session)
    produtos_comprados = []
    while(True):
        menu_compra()
        match input_int("Selecione uma opção: "):
            case 1:
                produto_id = input_int_positivo("Digite o ID do produto a ser adicionado: ")
                produto_encontrado = dic_produtos.get(produto_id)
                if produto_encontrado:
                        quantidade = input_int_positivo("Quantidade: ")
                        if (int(produto_encontrado.quantidade) >= quantidade):
                            dic_produtos[produto_encontrado.id_produto].quantidade = int(produto_encontrado.quantidade) - quantidade
                            preco_total = quantidade * float(produto_encontrado.preco)
                            produto_comprado = [produto_encontrado.id_produto ,produto_encontrado.nome, quantidade, produto_encontrado.preco, preco_total]
                            produtos_comprados.append(produto_comprado)
                        else:
                            print("Quantidade indisponível no estoque!")
                else:
                    print("Erro: produto não cadastrado.")
            case 2:
                break
            case _:
                print("Opção inválida!")
    produtos_comprados_agrupados = agrupar_itens_carrinho(produtos_comprados)
    return produtos_comprados_agrupados