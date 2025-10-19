import os.path
import sqlite3

def caminho_arquivo():
    BANCO = "./mercado.db"
    DIR = os.path.dirname(os.path.abspath(__file__))
    ARQ = os.path.join(DIR, BANCO)
    return ARQ

def conectar():
    conn = None
    try:
        conn = sqlite3.connect(caminho_arquivo())
    except Exception as ex:
        print(ex)
    return conn

def desconectar(conn):
    if conn:
        conn.close()