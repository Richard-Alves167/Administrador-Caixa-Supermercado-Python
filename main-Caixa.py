from Mercado_Caixa.caixa import abrir_caixa
from Common.conexao import conectar, desconectar

session = conectar()
print("Abrindo caixa...")
abrir_caixa(session)
desconectar(session)