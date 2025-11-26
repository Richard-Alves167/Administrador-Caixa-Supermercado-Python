from Common.crud.produtos import *
from Common.menus import *
from Common.conexao import conectar
from sqlalchemy import text
import pandas as pd

def visualizar_produto(session):
    produto_id = input("Digite o ID do produto: ")
    read_produto(session, produto_id)

def visualizar_produtos(session):
    read_produtos(session)

def adicionar_produto(session):
    produto = create_produto()
    insert_produto(session, produto)

def modificar_produto(session):
    produto_id = input("Digite o ID do produto a ser modificado: ")
    produto = return_produto(session, produto_id)
    if produto:
        menu_modificar_produto()
        opcao = input_int("Selecione uma opção: ")
        match opcao:
            case 1:
                update_produto_preco(session, produto_id)
            case 2:
                update_produto_quantidade(session, produto_id)
            case _:
                print("Opção inválida!")
    else:
        print("Produto não encontrado")

def deletar_produto(session):
    produto_id = input("Digite o ID do produto a ser deletado: ")
    delete_produto(session, produto_id)

def visualizar_produtos_mais_vendidos(session):
    conn = session.connection()
    query = "select p.id_produto as id, p.nome as produto, sum(i.quantidade) as quantidade_total_vendida from produto p inner join item i on p.id_produto = i.id_produto group by p.id_produto order by quantidade_total_vendida desc limit 5"
    df = pd.read_sql_query(query, conn)
    if df.empty:
        print("Nenhuma compra existente.")
    else:
        print(df.to_string(index=False))

def visualizar_produtos_menos_vendidos(session):
    conn = session.connection()
    query = "select p.id_produto as id, p.nome as produto, sum(i.quantidade) as quantidade_total_vendida from produto p inner join item i on p.id_produto = i.id_produto group by p.id_produto order by quantidade_total_vendida limit 5"
    df = pd.read_sql_query(query, conn)
    if df.empty:
        print("Nenhuma compra existente.")
    else:
        print(df.to_string(index=False))

def visualizar_produtos_pouco_estoque(session):
    conn = session.connection()
    quantidade_estoque_escolhido = input_int_positivo("Coloque o limite da quantidade de estoque para verificar os produtos: ")
    query = text("select id_produto as id, nome as produto, quantidade as quantidade_estoque from produto where quantidade_estoque <= :max_qtd order by quantidade_estoque desc")
    df = pd.read_sql_query(query, conn, params={"max_qtd": quantidade_estoque_escolhido})
    if df.empty:
        print("Nenhuma compra existente.")
    else:
        print(df.to_string(index=False))

def visualizar_produto_fornecedores(session):
    produto_id = input_int_positivo("Coloque o id do produto em que deseja verificar os fornecedores: ")
    produto = return_produto(session, produto_id)
    if produto:
        conn = session.connection()
        query = text("select f.id_fornecedor as id, f.nome as fornecedor from produto p inner join fornecedor_produto fp on p.id_produto = fp.id_produto inner join fornecedor f on fp.id_fornecedor = f.id_fornecedor where p.id_produto = :id_produto")
        df = pd.read_sql_query(query, conn, params={"id_produto": produto_id})
        if df.empty:
            print("Produto sem fornecedor.")
        else:
            print(df.to_string(index=False))
    else:
        print("ID de produto não cadastrado.")

def visualizar_produtos_sem_fornecedores(session):
    conn = session.connection()
    query = text("select p.id_produto as id, p.nome as produto from produto p left join fornecedor_produto fp on p.id_produto = fp.id_produto where fp.id_fornecedor is null")
    df = pd.read_sql_query(query, conn)
    if df.empty:
        print("Todos os produtos tem fornecedor.")
    else:
        print(df.to_string(index=False))