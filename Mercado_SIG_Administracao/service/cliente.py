from Common.crud.cliente import *
from Common.crud.compra import *
from Common.menus import *
from Common.models import *
from Common.util import visualizar_dataframe_tabulate_fancy_grid
from Mercado_Caixa.caixa import emitir_nota_fiscal
from sqlalchemy import text
import pandas as pd

def visualizar_cliente(session):
    cliente_id = input("Digite o ID do cliente: ")
    read_cliente(session, cliente_id)

def visualizar_clientes(session):
    read_clientes(session)

def visualizar_clientes_com_compras(session):
    conn = session.connection()
    query = "select distinct c.nome as cliente from cliente c inner join compra cp on c.id_cliente = cp.id_cliente"
    df = pd.read_sql_query(query, conn)
    if df.empty:
        print("Nenhum cliente com compras.")
    else:
        visualizar_dataframe_tabulate_fancy_grid(df, "Clientes com compras")

def visualizar_clientes_sem_compras(session):
    conn = session.connection()
    query = "select c.nome as cliente from cliente c left join compra cp on c.id_cliente = cp.id_cliente where cp.id_compra is null"
    df = pd.read_sql_query(query, conn)
    if df.empty:
        print("Todos clientes cadastrados possuem compra.")
    else:
        visualizar_dataframe_tabulate_fancy_grid(df, "Clientes sem compras")

def visualizar_cliente_compras(session):
    conn = session.connection()
    cliente_escolhido = input_int_positivo("Coloque o id do cliente em que deseja verificar as compras: ")
    cliente = return_cliente(session, cliente_escolhido)
    if cliente:
        query = text("select c.nome as cliente, cp.id_compra, cp.data_hora as data_compra, sum(i.preco_unitario * i.quantidade) as compra_total from cliente c inner join compra cp on c.id_cliente = cp.id_cliente inner join item i on i.id_compra = cp.id_compra where c.id_cliente = :id_cliente group by cp.id_compra order by data_compra desc")
        df = pd.read_sql_query(query, conn, params={"id_cliente": cliente_escolhido})
        if df.empty:
            print("Nenhuma compra existente.")
        else:
            visualizar_dataframe_tabulate_fancy_grid(df, "Compras de um cliente")
            soma_total_compras = df['compra_total'].sum()
            visualizar_total_abaixo_dataframe_tabulate_fancy_grid(df, cliente.nome, soma_total_compras)
            visualizar_cliente_compra(session)

def visualizar_cliente_compra(session):
    conn = session.connection()
    compra_escolhida = input_int_positivo("Coloque o id da compra em que deseja verificar a nota fiscal: ")
    compra = return_compra(session, compra_escolhida)
    if compra:
        #"id_produto", "nome", "quantidade", "preco_unitario","id_desconto", "quantidade_min_para_desconto", "percentual", "preco_subtotal", "desconto_total","preco_total"
        query = text("select p.id_produto, p.nome, i.quantidade, i.preco_unitario, i.id_desconto, i.quantidade_min_para_desconto, d.percentual, (i.quantidade * i.preco_unitario) as preco_subtotal, ((i.quantidade - i.quantidade_min_para_desconto) * i.preco_unitario * d.percentual) as desconto_total, (i.quantidade * i.preco_unitario) - (i.quantidade - i.quantidade_min_para_desconto) * i.preco_unitario as preco_total from item i inner join produto p on i.id_produto = p.id_produto inner join desconto d on i.id_desconto = d.id_desconto where i.id_compra = :id_compra")
        df = pd.read_sql_query(query, conn, params={"id_compra": compra_escolhida})
        if df.empty:
            print("Nenhum item existente para essa compra.")
        else:
            lista_produtos = []
            for index, item in df.iterrows():
                if item['quantidade_min_para_desconto'] >= item['quantidade']:
                    item['preco_total'] += item['desconto_total'] 
                    item['desconto_total'] = 0
                lista_produtos.append([item['id_produto'], item['nome'], item['quantidade'], item['preco_unitario'], item['id_desconto'], item['quantidade_min_para_desconto'], item['percentual'], item['preco_subtotal'], item['desconto_total'], item['preco_total']])
            atendimento = Atendimento(compra.id_cliente, compra.data_hora, lista_produtos)
            emitir_nota_fiscal(atendimento)

def visualizar_clientes_mais_compras(session):
    conn = session.connection()
    query = text("select c.nome as cliente, count(cp.id_compra) as quantidade_total_compras from cliente c inner join compra cp on c.id_cliente = cp.id_cliente group by c.id_cliente order by quantidade_total_compras desc limit 5")
    df = pd.read_sql_query(query, conn)
    if df.empty:
        print("Clientes sem compras.")
    else:
        visualizar_dataframe_tabulate_fancy_grid(df, "Clientes com mais compras")

def visualizar_clientes_mais_gasto(session):
    conn = session.connection()
    query = text("select c.nome as cliente, sum(i.preco_unitario * i.quantidade) as total_gasto from cliente c inner join compra cp on c.id_cliente = cp.id_cliente inner join item i on cp.id_compra = i.id_compra group by c.id_cliente order by total_gasto desc limit 5")
    df = pd.read_sql_query(query, conn)
    if df.empty:
        print("Clientes sem compras.")
    else:
        visualizar_dataframe_tabulate_fancy_grid(df, "Clientes com mais gasto no mercado")