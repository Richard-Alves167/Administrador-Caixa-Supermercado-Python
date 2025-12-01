from Common.util import *
from Common.crud.produto import *
from Common.crud.desconto import *
from Common.models import Atendimento
from Common.menus import *
from Common.log import *
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

def calcular_preco_subtotal(quantidade, preco_unitario):
    subtotal = quantidade * preco_unitario
    return subtotal

def calcular_desconto(session, quantidade_comprada, quantidade_minima, preco_unitario, id_desconto):
    if id_desconto != None and quantidade_comprada > quantidade_minima:
        desconto = return_desconto(session, id_desconto)
        percentual = desconto.percentual
        desconto = (quantidade_comprada - quantidade_minima) * preco_unitario * percentual
        return desconto, percentual
    return 0, 0

def calcular_preco_total(subtotal, desconto):
    total = subtotal - desconto
    return total

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
                            if dic_produtos[produto_encontrado.id_produto].quantidade == 0: criar_log_falta_estoque(produto_encontrado.id_produto, produto_encontrado.nome)
                            preco_subtotal = calcular_preco_subtotal(quantidade, float(produto_encontrado.preco))
                            desconto_total, percentual = calcular_desconto(session, quantidade, produto_encontrado.quantidade_min_para_desconto, produto_encontrado.preco, produto_encontrado.id_desconto)
                            preco_total = calcular_preco_total(preco_subtotal, desconto_total)
                            produto_comprado = [produto_encontrado.id_produto, produto_encontrado.nome, quantidade, produto_encontrado.preco, produto_encontrado.id_desconto, produto_encontrado.quantidade_min_para_desconto, percentual, preco_subtotal, desconto_total, preco_total]
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