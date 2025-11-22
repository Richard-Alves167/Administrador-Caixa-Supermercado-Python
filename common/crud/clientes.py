from common.models import Cliente
from common.util import *

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
            print(f"{cliente.id_cliente},{cliente.nome}")
        else:
            print("Cliente não encontrado.")
    except Exception as e:
        print("Erro:", e)

def read_clientes(session):
    print("Listar clientes")
    try:
        clientes = session.query(Cliente).all()
        for cliente in clientes:
            print(f"{cliente.id_cliente},{cliente.nome}")
    except Exception as e:
        print("Erro:", e)