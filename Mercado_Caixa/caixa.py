from Mercado_Caixa.crud.atendimentos import *
from Mercado_Caixa.service.atendimento import *
from Common.util import *
from Common.crud.produtos import *
from Common.crud.clientes import *
from Common.crud.compra import *
from Common.menus import *
from Mercado_Caixa.service.compra import *
from tabulate import tabulate

def emitir_nota_fiscal(atendimento):
    cliente = atendimento.id_cliente
    data = atendimento.data_criacao
    contador = 1
    total = 0
    itens_produto = atendimento.carrinho_produtos
    for item in itens_produto:
        total += item[4]
        contador += 1

    print(f"\nCLiente {cliente}")
    print(f"Data: {data}")
    print()
    cabecalho = ["Item", "Produto", "Quant."," Preço", "Total"]
    print(tabulate(itens_produto, headers=cabecalho))
    print()
    print(f"Itens: {len(itens_produto)}")
    print(f"Total: {total:.2f}")

def abrir_caixa(session):
    lista_atendimentos = []
    while(True):
        menu_atendimento()
        opcao = input_int("Selecione uma opção: ")
        match opcao:
            case 1:
                atendimento = atender_cliente(session)
                if (not atendimento == None):
                    update_estoque(session, atendimento.carrinho_produtos)
                    emitir_nota_fiscal(atendimento)
                    lista_atendimentos.append(atendimento)
                    salvar_compra(session, atendimento)
            case 2:
                fechar_caixa(session, lista_atendimentos)
                break
            case _:
                print("Opção inválida!")

def emitir_nota_clientes_atendidos(lista_atendimentos):
    lista_clientes_separados = []
    for atendimento in lista_atendimentos:
        nome_cliente = f"Cliente {atendimento.id_cliente}"
        total_cliente = sum([item[4] for item in atendimento.carrinho_produtos])
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

def verificar_produtos_indisponiveis(session):
    dic_produtos = return_produtos(session)
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

def fechar_caixa(session, lista_atendimentos):
    emitir_nota_clientes_atendidos(lista_atendimentos)
    verificar_produtos_indisponiveis(session)
    print("\nCaixa fechado com sucesso!\n")