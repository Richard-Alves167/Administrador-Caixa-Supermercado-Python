from Common.util import *
from Common.crud.produto import return_produto
from Mercado_SIG_Administracao.crud.fornecedor import return_fornecedor
from Common.models import Fornecedor_Produto

def insert_fornecedor_produto(session, fornecedor_id):
    try:
        fornecedor = return_fornecedor(session, fornecedor_id)
        if fornecedor:
            produto_id = input_int_positivo("Digite o ID do produto: ")
            produto = return_produto(session, produto_id)
            if produto and produto_id not in [p.id_produto for p in fornecedor.produtos]:
                fornecedor_produto = Fornecedor_Produto(int(fornecedor_id), int(produto_id))
                session.add(fornecedor_produto)
                session.commit()
                print("Fornecedor atualizado com sucesso!")
            else:
                print("Produto não cadastrado ou já vinculado ao fornecedor.")
    except Exception as e:
        print("Erro:", e)

def delete_fornecedor_produto(session, fornecedor_id):
    try:
        fornecedor = return_fornecedor(session, fornecedor_id)
        if fornecedor:
            produto_id = input_int_positivo("Digite o ID do produto: ")
            produto = return_produto(session, produto_id)
            if produto and produto_id in [p.id_produto for p in fornecedor.produtos]:
                session.delete(session.get(Fornecedor_Produto, (fornecedor_id, produto_id)))
                session.commit()
                print("Fornecedor atualizado com sucesso!")
            else:
                print("Produto não cadastrado ou já não está vinculado ao fornecedor.")
    except Exception as e:
        print("Erro:", e)

def insert_produto_fornecedor(session, produto_id):
    try:
        produto = return_produto(session, produto_id)
        if produto:
            fornecedor_id = input_int_positivo("Digite o ID do fornecedor: ")
            fornecedor = return_fornecedor(session, produto_id)
            if fornecedor and fornecedor_id not in [f.id_fornecedor for f in produto.fornecedores]:
                fornecedor_produto = Fornecedor_Produto(int(fornecedor_id), int(produto_id))
                session.add(fornecedor_produto)
                session.commit()
                print("Produto atualizado com sucesso!")
            else:
                print("Fornecedor não cadastrado ou já vinculado ao produto.")
    except Exception as e:
        print("Erro:", e)

def delete_produto_fornecedor(session, produto_id):
    try:
        produto = return_produto(session, produto_id)
        if produto:
            fornecedor_id = input_int_positivo("Digite o ID do fornecedor: ")
            fornecedor = return_fornecedor(session, fornecedor_id)
            if fornecedor and fornecedor_id in [f.id_fornecedor for f in produto.fornecedores]:
                session.delete(session.get(Fornecedor_Produto, (fornecedor_id, produto_id)))
                session.commit()
                print("Produto atualizado com sucesso!")
            else:
                print("Fornecedor não cadastrado ou já não está vinculado ao fornecedor.")
    except Exception as e:
        print("Erro:", e)