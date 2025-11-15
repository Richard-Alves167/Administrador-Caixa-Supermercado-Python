import pandas as pd

def agrupar_itens_carrinho(carrinho_produtos):
    df = pd.DataFrame(carrinho_produtos, columns=["id_produto", "nome", "quantidade", "preco_unitario", "preco_total"])
    df_agrupado = df.groupby(["id_produto", "nome", "preco_unitario"], as_index=False).agg({"quantidade": "sum", "preco_total": "sum"})
    df_agrupado = df_agrupado.reindex(columns=["id_produto", "nome", "quantidade", "preco_unitario", "preco_total"])
    carrinho_agrupado = df_agrupado.values.tolist()
    print(carrinho_agrupado)
    return carrinho_agrupado