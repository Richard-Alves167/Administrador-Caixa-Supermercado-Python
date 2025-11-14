from funcoes_caixa import *
from util_web_produtos import *

#abrir_sistema_supermercado()
lista = buscar_produtos_site()
for produto in lista:
    print(produto.nome, produto.preco, produto.quantidade)