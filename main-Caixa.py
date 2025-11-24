from Mercado_Caixa.caixa import abrir_caixa
from Common.conexao import conectar

session = conectar()
print("Abrindo caixa...")
abrir_caixa(session)