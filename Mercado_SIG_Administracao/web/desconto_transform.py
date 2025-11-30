def transformar_desconto_texto_para_id(texto_desconto):
    id_desconto = None
    match texto_desconto:
        case "bronze":
            id_desconto = 1
        case "prata":
            id_desconto = 2
        case "ouro":
            id_desconto = 3
        case "esmeralda":
            id_desconto = 4
        case "rubi":
            id_desconto = 5
        case "diamante":
            id_desconto = 6
    return id_desconto