import os.path
from util import *
from datetime import *
from models import Produto
from conexao import conectar, desconectar

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
    produtos = {}
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando)
        produtos = cursor.fetchall()
        if produtos:
            for produto in produtos:
                produtos[produto[0]] = Produto(produto[0], produto[1], produto[2], produto[3])
        return produtos
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
    try:
        with open(caminho_arquivo(), "w", encoding="utf-8") as arquivo:
            for index_dic in dic_produtos:
                produto = dic_produtos[index_dic]
                linha = str(produto) + "\n"
                arquivo.write(linha)
        print("Estoque atualizado com sucesso!")
    except Exception as e:
        print("Erro:", e)

def criar_tabela():
    comando = """
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    );
    """
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando)
        conn.commit()
    except Exception as e:
        print("Erro ao criar tabela:", e)
    finally:
        desconectar(conn)

def resetar_tabela():
    comando = "DROP TABLE IF EXISTS produto;"
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando)
        conn.commit()
        print("Tabela resetada com sucesso!")
    except Exception as e:
        print("Erro ao resetar tabela:", e)
    finally:
        desconectar(conn)

def mocki_produtos():
    produtos_mocki = [
        ("1", "Pitaya", 100, 9.99),
        ("2", "Uva", 30, 6.99),
        ("3", "Melancia", 300, 18.99),
        ("4", "Morango", 200, 4.99),
        ("5", "Carambola", 0, 23.99)
    ]
    comando = "insert into produto (id, nome, quantidade, preco) values (?, ?, ?, ?);"
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.executemany(comando, produtos_mocki)
        conn.commit()
    except Exception as e:
        print("Erro ao inserir produtos mocki:", e)
    finally:
        desconectar(conn)