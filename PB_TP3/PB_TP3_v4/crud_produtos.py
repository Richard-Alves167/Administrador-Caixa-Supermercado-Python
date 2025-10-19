import os.path
from util import *
from datetime import *
from models import Produto
from conexao import conectar, desconectar

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
    comando = "insert into produto (nome, quantidade, preco) values (?, ?, ?);"

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (produto.nome, produto.quantidade, produto.preco))
        conn.commit()
        print("Produto inserido com sucesso!")
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(conn)

def return_produto(produto_id):
    comando = "select * from produto where id = ?;"
    produto_encontrado = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (produto_id,))
        produto = cursor.fetchone()
        if produto:
            produto_encontrado = Produto(produto[0], produto[1], produto[2], produto[3])
        else:
            print("Erro: produto não cadastrado.")
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(conn)
    return produto_encontrado

def return_produtos():
    comando = "select * from produto;"

    produtos_dic = {}
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando)
        produtos = cursor.fetchall()
        for produto in produtos:
            produtos_dic[produto[0]] = Produto(produto[0], produto[1], produto[2], produto[3])
        return produtos_dic
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(conn)

def read_produto(produto_id):
    comando = "select * from produto where id = ?;"

    try:
        conn = conectar()
        cursor = conn.cursor()
        produto_encontrado = return_produto(produto_id)
        if produto_encontrado:
            cursor.execute(comando, (produto_id,))
            produto_encontrado = cursor.fetchone()
            produto_encontrado = Produto(produto_encontrado[0], produto_encontrado[1], produto_encontrado[2], produto_encontrado[3])
            print("Produto encontrado: ", produto_encontrado)
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(conn)

def read_produtos():
    comando = "select * from produto;"

    print("Listar produtos")
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando)
        produtos = cursor.fetchall()
        produtos = [Produto(produto[0], produto[1], produto[2], produto[3]) for produto in produtos]
        for produto in produtos:
            print(produto)
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(conn)

def update_produto_preco(produto_id):
    comando = "update produto set preco = ? where id = ?;"

    try:
        conn = conectar()
        cursor = conn.cursor()
        produto_encontrado = return_produto(produto_id)
        if produto_encontrado:
            novo_preco = input_float_positivo("Novo preço: ")
            cursor.execute(comando, (novo_preco, produto_id))
            conn.commit()
            print("Produto atualizado com sucesso!")
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(conn)

def update_produto_quantidade(produto_id):
    comando = "update produto set quantidade = ? where id = ?;"

    try:
        conn = conectar()
        cursor = conn.cursor()
        produto_encontrado = return_produto(produto_id)
        if produto_encontrado:
            nova_quantidade = input_int_positivo("Nova quantidade no estoque: ")
            cursor.execute(comando, (nova_quantidade, produto_id))
            conn.commit()
            print("Produto atualizado com sucesso!")
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(conn)

def delete_produto(produto_id):
    comando = "delete from produto where id = ?;"

    try:
        conn = conectar()
        cursor = conn.cursor()
        produto_encontrado = return_produto(produto_id)
        if produto_encontrado:
            cursor.execute(comando, (produto_id,))
            conn.commit()
            print("Produto deletado  com sucesso!")
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(conn)

def update_estoque(dic_produtos):
    comando = "update produto set quantidade = ? where id = ?;"

    try:
        conn = conectar()
        cursor = conn.cursor()
        for index_dic in dic_produtos:
            produto = dic_produtos[index_dic]
            cursor.execute(comando, (produto.quantidade, produto.id))
        conn.commit()
        print("Estoque atualizado com sucesso!")
    except Exception as e:
        print("Erro:", e)
    finally:
        desconectar(conn)