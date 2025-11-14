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
        return f"{self.id},{self.nome},{self.quantidade},{self.preco}"
    
class Cliente(declarative_base()):
    '''Classe que representa um cliente com ID e nome.'''

    __tablename__ = "cliente"

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"{self.id_cliente},{self.nome}"