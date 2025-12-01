from Common.crud.desconto import *
from Common.menus import *
from sqlalchemy import text
import pandas as pd

def visualizar_desconto(session):
    desconto_id = input("Digite o ID do desconto: ")
    read_desconto(session, desconto_id)

def visualizar_descontos(session):
    read_descontos(session)

def adicionar_desconto(session):
    desconto = create_desconto()
    insert_desconto(session, desconto)

def visualizar_desconto_com_produtos(session):
    conn = session.connection()
    query = "select distinct d.id_desconto as id, d.tier from desconto d inner join produto p on d.id_desconto = p.id_desconto"
    df = pd.read_sql_query(query, conn)
    if df.empty:
        print("Todos os descontos não tem nenhum produto.")
    else:
        print(df.to_string(index=False))

def visualizar_desconto_sem_produtos(session):
    conn = session.connection()
    query = "select d.id_desconto as id, d.tier from desconto d left join produto p on d.id_desconto = p.id_desconto where p.id_produto is null"
    df = pd.read_sql_query(query, conn)
    if df.empty:
        print("Todos os descontos tem algum produto.")
    else:
        print(df.to_string(index=False))

def visualizar_produtos_desconto(session):
    conn = session.connection()
    id_desconto = input_int_positivo("Coloque o id do desconto para verificar os produtos nesse desconto: ")
    query = text("select p.id_produto as id, p.nome as produto from desconto d inner join produto p on d.id_desconto = p.id_desconto where d.id_desconto = :id_desconto")
    df = pd.read_sql_query(query, conn, params={"id_desconto": id_desconto})
    if df.empty:
        print("Nenhum produto nesse desconto.")
    else:
        print(df.to_string(index=False))