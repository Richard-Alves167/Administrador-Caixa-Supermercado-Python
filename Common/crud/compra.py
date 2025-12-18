from Common.util import *
from Common.models import Compra
from datetime import *

def create_compra(atendimento):
    '''
    Cria uma nova compra.
    ID | Data compra
    '''
    compra = Compra(atendimento.id_cliente, atendimento.data_criacao)
    return compra

def insert_compra(session, compra):
    try:
        session.add(compra)
        session.commit()
        print("Compra inserido com sucesso!")
    except Exception as e:
        print("Erro:", e)

def return_compra(session, compra_id):
    compra_encontrado = None
    try:
        compra = session.query(Compra).get(compra_id)
        if compra:
            compra_encontrado = compra
        else:
            print("Erro: compra não cadastrado.")
    except Exception as e:
        print("Erro:", e)
    return compra_encontrado

def return_compras(session):
    compras_dic = {}
    try:
        compras = session.query(Compra).all()
        for compra in compras:
            compras_dic[compra.id_compra] = compra
    except Exception as e:
        print("Erro:", e)
    return compras_dic

def read_compra(session, compra_id):
    try:
        compra = return_compra(session, compra_id)
        if compra:
            visualizar_dataframe_um_dado_tabela(session, "compra", compra_id)
    except Exception as e:
        print("Erro:", e)

def read_compras(session):
    print("Listar compras")
    try:
        visualizar_dataframe_todos_dados_tabela(session, "compra")
    except Exception as e:
        print("Erro:", e)