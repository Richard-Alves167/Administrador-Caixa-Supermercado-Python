from Common.crud.compra import *

def salvar_compra(session, atendimento):
    compra = create_compra(atendimento)
    insert_compra(session, compra)