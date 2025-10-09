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