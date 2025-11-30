def transformar_desconto_texto_para_id(texto_desconto):
    id_desconto = None
    match texto_desconto:
        case "bronze":
            id_desconto = 1
        case "prata":
            id_desconto = 2
        case "ouro":
            id_desconto = 3
    return id_desconto