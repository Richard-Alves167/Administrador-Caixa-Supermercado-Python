from Common.models import Atendimento
from Mercado_Caixa.service.carrinho import adicionar_carrinho
from datetime import *

def create_atendimento(session, id_cliente):
    '''
    Cria um novo atendimento.
    Numero do Cliente | Data e Hora | Lista de Produtos Comprados [[ID, Nome, Quantidade, Preço, Quantidade Comprada]]
    '''

    print("Criar atendimento:")
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    produtos_comprados = adicionar_carrinho(session)
    atendimento = Atendimento(id_cliente, data, produtos_comprados)
    return atendimento