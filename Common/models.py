from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Cliente(Base):
    '''Classe que representa um cliente com ID e nome.'''

    __tablename__ = "cliente"

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    compras = relationship("Compra", cascade="all, delete")

    def __init__(self, id_cliente,nome):
        tamanho_palavra_cliente = len("Cliente")
        self.id_cliente = id_cliente
        if len(nome) > tamanho_palavra_cliente: 
            self.nome = nome
        else:
            self.nome = nome + " " + str(id_cliente)

    def __str__(self):
        return f"{self.id_cliente};{self.nome}"
    
class Compra(Base):
    '''Classe que representa uma compra com ID, ID do cliente e data da compra.'''

    __tablename__ = "compra"

    id_compra = Column(Integer, primary_key=True, autoincrement=True)
    data_hora = Column(String, nullable=False)
    id_cliente = Column(Integer, ForeignKey("cliente.id_cliente"))
    cliente = relationship("Cliente", back_populates="compras")
    itens = relationship("Item", cascade="all, delete")

    def __init__(self, id_cliente, data_hora):
        self.id_cliente = id_cliente
        self.data_hora = data_hora

    def __str__(self):
        return f"{self.id_cliente};{self.data_hora}"
    
class Desconto(Base):
    '''Classe que representa um desconto com ID, Tier e percentual.'''

    __tablename__ = "desconto"

    id_desconto = Column(Integer, primary_key=True, autoincrement=True)
    tier = Column(String, nullable=False)
    percentual = Column(Float, nullable=False)
    produtos = relationship("Produto", back_populates="desconto", passive_deletes=True)
    itens_descontados = relationship("Item", back_populates="desconto", passive_deletes=True)

    def __init__(self, tier, percentual):
        self.tier = tier
        self.percentual = percentual

    def __str__(self):
        return f"{self.id_desconto};{self.tier};{self.percentual}"

class Produto(Base):
    '''Classe que representa um produto com ID, nome, quantidade e preço.'''

    __tablename__ = "produto"

    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False) 
    quantidade_min_para_desconto = Column(Integer, nullable=True)
    id_desconto = Column(Integer, ForeignKey("desconto.id_desconto", ondelete='SET NULL'))
    desconto = relationship("Desconto", back_populates="produtos")
    vendas = relationship("Item", cascade="all, delete")
    fornecedores = relationship("Fornecedor", secondary="fornecedor_produto", back_populates="produtos")

    def __init__(self, nome, quantidade, preco, id_desconto=None, quantidade_min_para_desconto=3):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.id_desconto = id_desconto
        self.quantidade_min_para_desconto = quantidade_min_para_desconto

    def __str__(self):
        return f"{self.nome};{self.quantidade};{self.preco};{self.id_desconto};{self.quantidade_min_para_desconto}"

class Item(Base):
    '''Classe que representa um item de uma compra com ID, ID da compra ID do produto, quantidade comprada, preço do produto na hora da compra, desconto do produto na hora da compra e quantidade minima para ter desconto na hora da compra.'''

    __tablename__ = "item"

    id_item = Column(Integer, primary_key=True, autoincrement=True)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)
    quantidade_min_para_desconto = Column(Integer, nullable=True)
    id_compra = Column(Integer, ForeignKey("compra.id_compra"))
    id_produto = Column(Integer, ForeignKey("produto.id_produto"))
    id_desconto = Column(Integer, ForeignKey("desconto.id_desconto"), nullable=True)
    compra = relationship("Compra", back_populates="itens")
    venda = relationship("Produto", back_populates="vendas")
    desconto = relationship("Desconto", back_populates="itens_descontados", passive_deletes=True)

    def __init__(self, id_compra, id_produto, quantidade, preco_unitario, id_desconto, quantidade_min_para_desconto):
        self.id_compra = id_compra
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.id_desconto = id_desconto
        self.quantidade_min_para_desconto = quantidade_min_para_desconto

    def __str__(self):
        return f"{self.id_cliente};{self.id_compra};{self.id_item};{self.id_produto};{self.quantidade};{self.preco_unitario};{self.id_desconto};{self.quantidade_min_para_desconto}"
    
class Fornecedor(Base):
    '''Classe que representa um fornecedor com ID e nome.'''

    __tablename__ = "fornecedor"

    id_fornecedor = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    produtos = relationship("Produto", secondary="fornecedor_produto", back_populates="fornecedores", cascade="all, delete")

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"{self.id_fornecedor};{self.nome}"

class Fornecedor_Produto(Base):
    '''Classe auxiliar de banco de dados que representa o fornecimento de um produto com ID de fornecedor e ID de produto.'''

    __tablename__ = "fornecedor_produto"

    id_fornecedor = Column(Integer, ForeignKey("fornecedor.id_fornecedor"), primary_key=True)
    id_produto = Column(Integer, ForeignKey("produto.id_produto"), primary_key=True)

    def __init__(self, id_fornecedor, id_produto):
        self.id_fornecedor = id_fornecedor
        self.id_produto = id_produto

    def __str__(self):
        return f"{self.id_fornecedor};{self.id_produto}"

class Atendimento():
    '''Classe que representa um atendimento com número do cliente, data e hora, e lista de produtos comprados.'''

    def __init__(self, id_cliente, data_criacao, carrinho_produtos):
        self.id_cliente = id_cliente
        self.data_criacao = data_criacao
        self.carrinho_produtos = carrinho_produtos

    def __str__(self):
        return f"{self.id_cliente};{self.data_hora};{self.carrinho_produtos}"