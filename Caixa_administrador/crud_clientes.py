from models import Cliente

def read_clientes(session):
    print("Listar clientes")
    try:
        clientes = session.query(Cliente).all()
        for cliente in clientes:
            print(f"{cliente.id_cliente},{cliente.nome}")
    except Exception as e:
        print("Erro:", e)