import os.path
from util import *
from datetime import *
from models import Produto

def caminho_arquivo():
    ARQ = "produtos.csv"
    DIR = os.path.dirname(os.path.abspath(__file__))
    ARQ = os.path.join(DIR, ARQ)
    return ARQ


def create_produto():
    '''
    Cria um novo produto.
    ID | Nome | Quantidade | Preço  
    '''

    print("Criar produto:")
    id = datetime.now().strftime("%Y%m%d%H%M%S%f")
    nome = input("Nome: ")
    quantidade = input_int_positivo("Quantidade: ")
    preco = input_float_positivo("Preço: ")
    produto = Produto(id, nome, quantidade, preco)
    print("Produto criado com sucesso!")
    return produto

def insert_produto(produto):
    try:
        with open(caminho_arquivo(), "a", encoding="utf-8") as arquivo:
            linha = str(produto) + "\n"
            arquivo.write(linha)
            print("Produto inserido com sucesso!")
    except Exception as e:
        print("Erro:", e)

def return_produto(produto_id):
    try:
        with open(caminho_arquivo(), "r", encoding="utf-8") as arquivo:
            produtos = [linha.strip().split(",") for linha in arquivo.readlines()]
            produtos = [Produto(produto[0], produto[1], produto[2], produto[3]) for produto in produtos]
            produto_encontrado = None
            for produto in produtos:
                if (produto.id == produto_id):
                    produto_encontrado = produto
                    break
            return produto_encontrado
    except Exception as e:
        print("Erro:", e)

def return_produtos():
    try:
        with open(caminho_arquivo(), "r", encoding="utf-8") as arquivo:
            produtos = {}
            for linha in arquivo.readlines():
                produto_array = linha.strip().split(",")
                produto = Produto(produto_array[0], produto_array[1], produto_array[2], produto_array[3])
                produtos[produto.id] = produto
            return produtos
    except Exception as e:
        print("Erro:", e)

def read_produto(produto_id):
    print("Procurar produto de ID:", produto_id)
    try:
        with open(caminho_arquivo(), "r", encoding="utf-8") as arquivo:
            produtos = [linha.strip().split(",") for linha in arquivo.readlines()]
            produtos = [Produto(produto[0], produto[1], produto[2], produto[3]) for produto in produtos]
            produto_encontrado = None
            for produto in produtos:
                if (produto.id == produto_id):
                    produto_encontrado = produto
                    break
            if produto_encontrado:
                print("Produto encontrado: ", produto_encontrado)
            else:
                print("Produto não encontrado")
    except Exception as e:
        print("Erro:", e)

def read_produtos():
    print("Listar produtos")
    try:
        with open(caminho_arquivo(), "r", encoding="utf-8") as arquivo:
            produtos = [linha.strip().split(",") for linha in arquivo.readlines()]
            produtos = [Produto(produto[0], produto[1], produto[2], produto[3]) for produto in produtos]
        for produto in produtos:
            print(produto)
    except Exception as e:
        print("Erro:", e)

def update_produto_preco(produto_id):
    try:
        with open(caminho_arquivo(), "r", encoding="utf-8") as arquivo:
            produtos = [linha.strip().split(",") for linha in arquivo.readlines()]
            produtos = [Produto(produto[0], produto[1], produto[2], produto[3]) for produto in produtos]
            linha_arquivo = 0
            produto_encontrado = None
            for index, produto in enumerate(produtos):
                if (produto.id == produto_id):
                    produto_encontrado = produto
                    linha_arquivo = index
                    break
            if produto_encontrado:
                novo_preco = input_float_positivo("Novo preço: ")
                produtos[linha_arquivo].preco = novo_preco
                with open(caminho_arquivo(), "w", encoding="utf-8") as arquivo:
                    for produto in produtos:
                        linha = str(produto) + "\n"
                        arquivo.write(linha)
                print("Produto atualizado com sucesso!")
            else:
                print("Produto não encontrado")
    except Exception as e:
        print("Erro:", e)

def update_produto_quantidade(produto_id):
    try:
        with open(caminho_arquivo(), "r", encoding="utf-8") as arquivo:
            produtos = [linha.strip().split(",") for linha in arquivo.readlines()]
            produtos = [Produto(produto[0], produto[1], produto[2], produto[3]) for produto in produtos]
            linha_arquivo = 0
            produto_encontrado = None
            for index, produto in enumerate(produtos):
                if (produto.id == produto_id):
                    produto_encontrado = produto
                    linha_arquivo = index
                    break
            if produto_encontrado:
                nova_quantidade = input_int_positivo("Nova quantidade no estoque: ")
                produtos[linha_arquivo].quantidade = nova_quantidade
                with open(caminho_arquivo(), "w", encoding="utf-8") as arquivo:
                    for produto in produtos:
                        linha = produto.__str__() + "\n"
                        arquivo.write(linha)
                print("Produto atualizado com sucesso!")
            else:
                print("Produto não encontrado")
    except Exception as e:
        print("Erro:", e)

def delete_produto(produto_id):
    try:
        with open(caminho_arquivo(), "r", encoding="utf-8") as arquivo:
            produtos = [linha.strip().split(",") for linha in arquivo.readlines()]
            produtos = [Produto(produto[0], produto[1], produto[2], produto[3]) for produto in produtos]
            linha_arquivo = 0
            produto_encontrado = None
            for index, produto in enumerate(produtos):
                if (produto.id == produto_id):
                    produto_encontrado = produto
                    linha_arquivo = index
                    break
            if produto_encontrado:
                produtos.pop(linha_arquivo)
                with open(caminho_arquivo(), "w", encoding="utf-8") as arquivo:
                    for produto in produtos:
                        linha = str(produto) + "\n"
                        arquivo.write(linha)
                print("Produto deletado  com sucesso!")
            else:
                print("Produto não encontrado")
    except Exception as e:
        print("Erro:", e)

def update_estoque(dic_produtos):
    try:
        with open(caminho_arquivo(), "w", encoding="utf-8") as arquivo:
            for index_dic in dic_produtos:
                produto = dic_produtos[index_dic]
                linha = str(produto) + "\n"
                arquivo.write(linha)
        print("Estoque atualizado com sucesso!")
    except Exception as e:
        print("Erro:", e)