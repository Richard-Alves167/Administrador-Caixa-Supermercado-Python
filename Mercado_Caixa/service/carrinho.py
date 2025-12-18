from Common.util import *
from Common.crud.produto import *
from Common.crud.desconto import *
from Common.menus import *
from Common.models import Item_Carrinho_Calculado
import pandas as pd

def agrupar_itens_carrinho(carrinho_produtos):
    df = pd.DataFrame(carrinho_produtos, columns=["id_produto", "nome", "quantidade", "preco_unitario", "id_desconto", "quantidade_min_para_desconto"])
    df_agrupado = df.groupby(["id_produto", "nome", "preco_unitario", "id_desconto", "quantidade_min_para_desconto"], as_index=False).agg({"quantidade": "sum"})
    df_agrupado = df_agrupado.reindex(columns=["id_produto", "nome", "quantidade", "preco_unitario","id_desconto", "quantidade_min_para_desconto"])
    carrinho_agrupado = df_agrupado.values.tolist()
    return carrinho_agrupado

def selecionar_produto(session, dic_produto_estoque):
    produto_comprado = None
    produto_id = input_int_positivo("Digite o ID do produto a ser adicionado: ")
    produto = return_produto(session, produto_id)
    if produto:
        quantidade = input_int_positivo("Quantidade: ")
        if (dic_produto_estoque[produto_id] >= quantidade):
            dic_produto_estoque[produto_id] -= quantidade
            if dic_produto_estoque[produto_id] == 0: criar_log_falta_estoque(produto.id_produto, produto.nome)
            produto_comprado = [produto.id_produto, produto.nome, quantidade, produto.preco, produto.id_desconto, produto.quantidade_min_para_desconto]
        else:
            print("Quantidade indisponível no estoque!")
    else:
        print("Erro: produto não cadastrado.")
    return produto_comprado

def calcular_desconto_carrinho(session, carrinho_produtos):
    produtos_calculo_total = []
    for produto in carrinho_produtos:
        produto_calculado = None
        if produto[3] != None:
            desconto = return_desconto(session, produto[4])
            produto_calculado = Item_Carrinho_Calculado(produto[0], produto[1], produto[2], produto[3], produto[4], desconto.percentual, produto[5])
        else:
            produto_calculado = Item_Carrinho_Calculado(produto[0], produto[1], produto[2], produto[3], produto[4], 0, produto[5])
        produtos_calculo_total.append(produto_calculado)
    return produtos_calculo_total

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
    produtos_agrupados_calculados = calcular_desconto_carrinho(session, produtos_comprados_agrupados)
    return produtos_agrupados_calculados