from sqlalchemy import Column, Integer, String, Float, BIGINT
from sqlalchemy.ext.declarative import declarative_base

class Produto(declarative_base()):
    '''Classe que representa um produto com ID, nome, quantidade e preço.'''

    __tablename__ = "produto"

    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)

    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"{self.nome};{self.quantidade};{self.preco}"
    
class Cliente(declarative_base()):
    '''Classe que representa um cliente com ID e nome.'''

    __tablename__ = "cliente"

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    def __init__(self, id_cliente,nome):
        tamanho_palavra_cliente = len("Cliente")
        self.id_cliente = id_cliente
        if len(nome) > tamanho_palavra_cliente: 
            self.nome = nome
        else:
            self.nome = nome + " " + str(id_cliente)

    def __str__(self):
        return f"{self.id_cliente};{self.nome}"
    
class Atendimento():
    '''Classe que representa um atendimento com número do cliente, data e hora, e lista de produtos comprados.'''

    def __init__(self, id_cliente, data_criacao, carrinho_produtos):
        self.id_cliente = id_cliente
        self.data_criacao = data_criacao
        self.carrinho_produtos = carrinho_produtos

    def __str__(self):
        return f"{self.id_cliente};{self.data_hora};{self.carrinho_produtos}"