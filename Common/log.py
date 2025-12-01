from datetime import datetime

def criar_log_falta_estoque(id_produto, nome):
    try:
        arquivo = open("Common/datasets/logs/falta_em_estoque.txt", "a", encoding="utf-8")
        arquivo.write(f"{datetime.now().strftime("%d/%m/%Y %H:%M")} -> Estoque esgotado: ID: {id_produto} - {nome}\n")
        arquivo.close()
    except Exception as e:
        print("Erro ao criar log de esgotamento de estoque:", e)

def criar_log_atualizacao_preco(id_produto, nome, preco_antigo, preco_novo):
    try:
        arquivo = open("Common/datasets/logs/atualizacao_preco_produto.txt", "a", encoding="utf-8")
        arquivo.write(f"{datetime.now().strftime("%d/%m/%Y %H:%M")} -> Produto com preço atualizado: ID {id_produto} - {nome} | {preco_antigo} -> {preco_novo}\n")
        arquivo.close()
    except Exception as e:
        print("Erro ao criar log de esgotamento de estoque:", e)