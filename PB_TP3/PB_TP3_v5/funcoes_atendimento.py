from util import *
from crud_produtos import *
from crud_atendimentos import *
from menus import *
from tabulate import tabulate

def atender_cliente():
    atendimento = create_atendimento()
    if (not atendimento[2] == []):
        return atendimento
    else: 
        print("Erro: Atendimento/Carrinho sem produtos...")
        return None

def emitir_nota_fiscal(atendimento):
    cliente = atendimento[0]
    data = atendimento[1]
    contador = 1
    total = 0
    produtos = []
    for item in atendimento[2]:
        produtos.append([contador, item[1], item[2], item[3], item[4]])
        total += item[4]
        contador += 1

    print(f"CLiente {cliente}")
    print(f"Data: {data}")
    print()
    cabecalho = ["Item", "Produto", "Quant."," Preço", "Total"]
    print(tabulate(produtos, headers=cabecalho))
    print()
    print(f"Itens: {len(produtos)}")
    print(f"Total: {total:.2f}")

def abrir_caixa():
    lista_atendimentos = []
    while(True):
        menu_atendimento()
        opcao = input_int("Selecione uma opção: ")
        match opcao:
            case 1:
                atendimento = atender_cliente()
                if (not atendimento == None):
                    atendimento[0] = len(lista_atendimentos) + 1
                    emitir_nota_fiscal(atendimento)
                    lista_atendimentos.append(atendimento)
            case 2:
                fechar_caixa(lista_atendimentos)
                break
            case _:
                print("Opção inválida!")


def emitir_nota_clientes_atendidos(lista_clientes):
    lista_clientes_separados = []
    for cliente in lista_clientes:
        nome_cliente = f"Cliente {cliente[0]}"
        total_cliente = sum([produto[4] for produto in cliente[2]])
        lista_clientes_separados.append([nome_cliente, total_cliente])
    total = sum([cliente[1] for cliente in lista_clientes_separados])

    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    print("Fechamento do caixa\n")
    print(f"Data: {data}")
    print()
    cabecalho = ["Cliente", "Total"]
    print(tabulate(lista_clientes_separados, headers=cabecalho))
    print()
    print(f"Total: {total:.2f}")

def verificar_produtos_indisponiveis():
    dic_produtos = return_produtos()
    produtos_indisponiveis = []
    for index_dic in dic_produtos:
        produto = dic_produtos[index_dic]
        if int(produto.quantidade) == 0:
            produtos_indisponiveis.append(produto)
    if (not produtos_indisponiveis == []):
        print("\nProdutos sem estoque:")
        for produto in produtos_indisponiveis:
            print(produto.nome)
    else:
        print("Todos os produtos estão com estoque disponível.")


def fechar_caixa(lista_atendimentos):
    emitir_nota_clientes_atendidos(lista_atendimentos)
    verificar_produtos_indisponiveis()
    print("\nCaixa fechado com sucesso!\n")