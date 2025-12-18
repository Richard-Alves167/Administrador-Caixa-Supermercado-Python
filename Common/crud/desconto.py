from Common.models import Desconto
from Common.util import *

def create_desconto():
    '''
    Cria um novo desconto.
    ID | Tier | Percentual 
    '''
    print("Cadastrando Desconto...")
    tier = input("Tier: ")
    percentual = input_int_positivo_entre_1_e_100("Percentual de desconto em inteiro: ")
    percentual = percentual/100
    desconto = Desconto(tier, percentual)
    print("Desconto criado com sucesso!")
    return desconto

def insert_desconto(session, desconto):
    try:
        session.add(desconto)
        session.commit()
        print("Desconto inserido com sucesso!")
    except Exception as e:
        print("Erro:", e)

def return_desconto(session, id_desconto):
    desconto_encontrado = None
    try:
        desconto = session.query(Desconto).get(id_desconto)
        if desconto:
            desconto_encontrado = desconto
        else:
            print("Desconto não cadastrado.")
    except Exception as e:
        print("Erro:", e)
    return desconto_encontrado

def read_desconto(session, id_desconto):
    try:
        desconto = return_desconto(session, id_desconto)
        if desconto:
            visualizar_dataframe_um_dado_tabela(session, "desconto", id_desconto)
        else:
            print("Desconto não encontrado.")
    except Exception as e:
        print("Erro:", e)

def read_descontos(session):
    print("Listar descontos")
    try:
        visualizar_dataframe_todos_dados_tabela(session, "desconto")
    except Exception as e:
        print("Erro:", e)

def delete_desconto(session, desconto_id):
    try:
        desconto = return_desconto(session, desconto_id)
        if desconto:
            session.delete(desconto)
            session.commit()
            print("Desconto deletado com sucesso!")
    except Exception as e:
        print("Erro:", e)