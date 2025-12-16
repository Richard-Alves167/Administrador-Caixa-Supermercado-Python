from Common.util import *
from Common.crud.produto import *
from Common.crud.desconto import *
from Common.menus import *
from Mercado_Caixa.data.tabela import agrupar_itens_carrinho

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
    dic_produto_estoque = return_produto_estoque(session)
    produtos_comprados = []
    while(True):
        menu_compra()
        match input_int("Selecione uma opção: "):
            case 1:
                produto = selecionar_produto(session, dic_produto_estoque)
                if produto:
                    produtos_comprados.append(produto)
            case 2:
                break
            case _:
                print("Opção inválida!")
    produtos_comprados_agrupados = agrupar_itens_carrinho(produtos_comprados)
    return produtos_comprados_agrupados

def selecionar_produto(session, dic_produto_estoque):
    produto_comprado = None
    produto_id = input_int_positivo("Digite o ID do produto a ser adicionado: ")
    produto = return_produto(session, produto_id)
    if produto:
        quantidade = input_int_positivo("Quantidade: ")
        if (dic_produto_estoque[produto_id] >= quantidade):
            dic_produto_estoque[produto_id] -= quantidade
            if dic_produto_estoque[produto_id] == 0: criar_log_falta_estoque(produto.id_produto, produto.nome)
            preco_subtotal = calcular_preco_subtotal(quantidade, float(produto.preco))
            desconto_total, percentual = calcular_desconto(session, quantidade, produto.quantidade_min_para_desconto, produto.preco, produto.id_desconto)
            preco_total = calcular_preco_total(preco_subtotal, desconto_total)
            produto_comprado = [produto.id_produto, produto.nome, quantidade, produto.preco, produto.id_desconto, produto.quantidade_min_para_desconto, percentual, preco_subtotal, desconto_total, preco_total]
        else:
            print("Quantidade indisponível no estoque!")
    else:
        print("Erro: produto não cadastrado.")
    return produto_comprado