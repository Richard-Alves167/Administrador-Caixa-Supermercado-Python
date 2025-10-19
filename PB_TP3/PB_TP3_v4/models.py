class Produto:
    '''Classe que representa um produto com ID, nome, quantidade e preço.'''

    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"{self.id},{self.nome},{self.quantidade},{self.preco}"