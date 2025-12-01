import pandas as pd

def agrupar_itens_carrinho(carrinho_produtos):
    df = pd.DataFrame(carrinho_produtos, columns=["id_produto", "nome", "quantidade", "preco_unitario", "id_desconto", "quantidade_min_para_desconto", "percentual", "preco_subtotal", "desconto_total","preco_total"])
    df_agrupado = df.groupby(["id_produto", "nome", "preco_unitario", "id_desconto", "quantidade_min_para_desconto", "percentual"], as_index=False).agg({"quantidade": "sum", "preco_subtotal": "sum", "desconto_total": "sum", "preco_total": "sum"})
    df_agrupado = df_agrupado.reindex(columns=["id_produto", "nome", "quantidade", "preco_unitario","id_desconto", "quantidade_min_para_desconto", "percentual", "preco_subtotal", "desconto_total","preco_total"])
    carrinho_agrupado = df_agrupado.values.tolist()
    return carrinho_agrupado