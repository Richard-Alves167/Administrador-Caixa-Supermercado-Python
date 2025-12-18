from tabulate import tabulate

def input_int(msg):
    parar_loop = False
    while(not parar_loop):
        try:
            valor = int(input(msg))
            parar_loop = True
        except:
            print("Valor inválido!\nTente novamente...")
    return valor

def input_int_positivo(msg):
    parar_loop = False
    while(not parar_loop):
        try:
            valor = int(input(msg))
            if (valor <= 0):
                raise ValueError("Error: número negativo")
            parar_loop = True
        except:
            print("Valor inválido!\nTente novamente...")
    return valor

def input_int_positivo_entre_1_e_100(msg):
    parar_loop = False
    while(not parar_loop):
        try:
            valor = int(input(msg))
            if (valor <= 0 or valor > 100):
                raise ValueError("Error: número fora dos limites de porcentagem")
            parar_loop = True
        except:
            print("Valor inválido!\nTente novamente...")
    return valor

def input_float(msg):
    parar_loop = False
    while(not parar_loop):
        try:
            valor = float(input(msg))
            parar_loop = True
        except:
            print("Valor inválido!\nTente novamente...")
    return valor

def input_float_positivo(msg):
    parar_loop = False
    while(not parar_loop):
        try:
            valor = float(input(msg))
            if (valor <= 0):
                raise ValueError("Error: número negativo")
            parar_loop = True
        except:
            print("Valor inválido!\nTente novamente...")
    return valor 

def retirar_underscore_colunas_tabela_string(lista_colunas_tabela):
    lista_formatada = [coluna.replace("_"," ") for coluna in lista_colunas_tabela]
    return lista_formatada

def printar_titulo_dataframe_tabulate_fancy_grid(tabela, titulo):
    linhas = tabela.splitlines()
    largura_tabela = len(linhas[0])
    largura_titulo = len(titulo) + 2
    largura_final = max(largura_tabela, largura_titulo)
    topo_titulo = "╒" + "═" * (largura_final - 2) + "╕"
    meio_titulo = "│" + titulo.center(largura_final - 2) + "│"
    base_titulo = "╘" + "═" * (largura_final - 2) + "╛"
    print(topo_titulo)
    print(meio_titulo)
    print(base_titulo)

def visualizar_dataframe_tabulate_fancy_grid(dataframe, titulo):
    lista_nome_colunas = dataframe.columns.tolist()
    cabecalho = retirar_underscore_colunas_tabela_string(lista_nome_colunas)
    tabela = tabulate(dataframe, headers=cabecalho, tablefmt="fancy_grid", showindex=False)
    printar_titulo_dataframe_tabulate_fancy_grid(tabela, titulo)
    print(tabela)

def visualizar_total_abaixo_dataframe_tabulate_fancy_grid(dataframe, cliente, total_gasto):
    tabela = tabulate(dataframe, tablefmt="fancy_grid", showindex=False)
    texto = f"Total gasto pelo {cliente}: {total_gasto:.2f}"
    linhas = tabela.splitlines()
    largura_tabela = len(linhas[0])
    largura_texto = len(texto) + 2
    largura_final = max(largura_tabela, largura_texto)
    topo_texto = "╒" + "═" * (largura_final - 2) + "╕"
    meio_texto = "│" + texto.center(largura_final - 2) + "│"
    base_texto = "╘" + "═" * (largura_final - 2) + "╛"
    print(topo_texto)
    print(meio_texto)
    print(base_texto)

def sair(frase):
    print(frase)