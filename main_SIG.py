from Mercado_SIG_Administracao.sig import acessar_area_administrador
from Common.conexao import conectar

from Common.models import *

session = conectar()
print("Entrando no sistema SIG...")
acessar_area_administrador(session)