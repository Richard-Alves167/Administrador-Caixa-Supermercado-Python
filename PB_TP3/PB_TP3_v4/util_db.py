from conexao import conectar, desconectar

def criar_tabela():
    comando = """
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    );
    """
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando)
        conn.commit()
    except Exception as e:
        print("Erro ao criar tabela:", e)
    finally:
        desconectar(conn)

def resetar_tabela():
    comando = "DROP TABLE IF EXISTS produto;"
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando)
        conn.commit()
        print("Tabela resetada com sucesso!")
    except Exception as e:
        print("Erro ao resetar tabela:", e)
    finally:
        desconectar(conn)

def mocki_produtos():
    produtos_mocki = [
        ("1", "Pitaya", 100, 9.99),
        ("2", "Uva", 30, 6.99),
        ("3", "Melancia", 300, 18.99),
        ("4", "Morango", 200, 4.99),
        ("5", "Carambola", 0, 23.99)
    ]
    comando = "insert into produto (id, nome, quantidade, preco) values (?, ?, ?, ?);"
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.executemany(comando, produtos_mocki)
        conn.commit()
    except Exception as e:
        print("Erro ao inserir produtos mocki:", e)
    finally:
        desconectar(conn)