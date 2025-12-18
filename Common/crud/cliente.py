from Common.models import Cliente
from Common.util import *

def create_cliente(id_cliente):
    '''
    Cria um novo cliente.
    ID | Nome 
    '''
    print("Cadastrando Cliente...")
    nome = "Cliente"
    cliente = Cliente(id_cliente, nome)
    print("Cliente criado com sucesso!")
    return cliente

def insert_cliente(session, cliente):
    try:
        session.add(cliente)
        session.commit()
        print("Cliente inserido com sucesso!")
    except Exception as e:
        print("Erro:", e)

def return_cliente(session, id_cliente):
    cliente_encontrado = None
    try:
        cliente = session.query(Cliente).get(id_cliente)
        if cliente:
            cliente_encontrado = cliente
        else:
            print("Cliente não cadastrado.")
    except Exception as e:
        print("Erro:", e)
    return cliente_encontrado

def read_cliente(session, id_cliente):
    try:
        cliente = return_cliente(session, id_cliente)
        if cliente:
            visualizar_dataframe_um_dado_tabela(session, "cliente", id_cliente)
        else:
            print("Cliente não encontrado.")
    except Exception as e:
        print("Erro:", e)

def read_clientes(session):
    print("Listar clientes")
    try:
        visualizar_dataframe_todos_dados_tabela(session, "cliente")
    except Exception as e:
        print("Erro:", e)