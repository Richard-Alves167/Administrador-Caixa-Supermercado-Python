from Mercado_SIG_Administracao.crud.fornecedor import *
from Common.menus import *
from sqlalchemy import text
import pandas as pd

def visualizar_fornecedor(session):
    fornecedor_id = input("Digite o ID do fornecedor: ")
    read_fornecedor(session, fornecedor_id)

def visualizar_fornecedores(session):
    read_fornecedores(session)

def adicionar_fornecedor(session):
    fornecedor = create_fornecedor()
    insert_fornecedor(session, fornecedor)

def modificar_fornecedor(session):
    fornecedor_id = input("Digite o ID do fornecedor a ser modificado: ")
    fornecedor = return_fornecedor(session, fornecedor_id)
    if fornecedor:
        print("Fornecedor encontrado:", fornecedor.nome)
        menu_modificar_fornecedor()
        opcao = input_int("Selecione uma opção: ")
        match opcao:
            case 1:
                insert_fornecedor_produto(session, fornecedor_id)
            case 2:
                delete_fornecedor_produto(session, fornecedor_id)
            case 3:
                sair("Saindo da opção de modificação de fornecedor...")
            case _:
                print("Opção inválida!")
    else:
        print("fornecedor não encontrado")

def deletar_fornecedor(session):
    fornecedor_id = input("Digite o ID do fornecedor a ser deletado: ")
    delete_fornecedor(session, fornecedor_id)

def visualizar_fornecedores_com_produtos(session):
    conn = session.connection()
    query = "select distinct f.id_fornecedor, f.nome as fornecedor from fornecedor f inner join fornecedor_produto fp on f.id_fornecedor = fp.id_fornecedor"
    df = pd.read_sql_query(query, conn)
    if df.empty:
        print("Todos os fornecedores não distribuem nenhum produto.")
    else:
        print(df.to_string(index=False))

def visualizar_fornecedores_sem_produtos(session):
    conn = session.connection()
    query = "select distinct f.id_fornecedor, f.nome as fornecedor from fornecedor f left join fornecedor_produto fp on f.id_fornecedor = fp.id_fornecedor where fp.id_produto is null"
    df = pd.read_sql_query(query, conn)
    if df.empty:
        print("Todos os fornecedores distribuem algum produto.")
    else:
        print(df.to_string(index=False))

def visualizar_produtos_fornecedor(session):
    fornecedor_id = input_int_positivo("Coloque o id do fornecedor em que deseja verificar os produtos: ")
    fornecedor = return_fornecedor(session, fornecedor_id)
    if fornecedor:
        conn = session.connection()
        query = text("select p.id_produto as id, p.nome as produto from produto p inner join fornecedor_produto fp on p.id_produto = fp.id_produto inner join fornecedor f on fp.id_fornecedor = f.id_fornecedor where f.id_fornecedor = :id_fornecedor")
        df = pd.read_sql_query(query, conn, params={"id_fornecedor": fornecedor_id})
        if df.empty:
            print("Fornecedor sem produtos.")
        else:
            print(df.to_string(index=False))
    else:
        print("ID de fornecedor não cadastrado.")