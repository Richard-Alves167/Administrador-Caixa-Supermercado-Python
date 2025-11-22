from Mercado_Caixa.crud.atendimentos import *
from common.util import *
from common.crud.produtos import *
from common.crud.clientes import *

def escolher_cliente(session):
    id_cliente = input_int_positivo("Selecione o ID do cliente: ")
    cliente = return_cliente(session, id_cliente)
    if not cliente:
        cliente = create_cliente(id_cliente)
        insert_cliente(session, cliente)
        id_cliente = cliente.id_cliente
    print(f"Cliente selecionado - {cliente.nome}")
    return id_cliente

def atender_cliente(session):
    id_cliente = escolher_cliente(session)
    atendimento = create_atendimento(session, id_cliente)
    if (not atendimento.carrinho_produtos == []):
        return atendimento
    else: 
        print("Atendimento cancelado -> Carrinho sem produtos...")
        return None