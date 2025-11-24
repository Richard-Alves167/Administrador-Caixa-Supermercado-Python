from Common.models import Produto
from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = "https://pedrovncs.github.io/lindosprecos/produtos.html#"

def acessar_url(URL):
    try:
        html = urlopen(URL)
    except Exception as ex:
        print(ex)
        exit()
    return html

def retornar_html_parse(html):
    try:
        bs = BeautifulSoup(html, 'html.parser')
    except Exception as ex:
        print(ex)
        exit()
    return bs

def obter_lista_produtos(bs):
    lista_produtos = []
    try:
        lista_produtos_card_html = bs.find('div',id='produtos-lista').find_all('div',class_='product-item')
        lista_body_produtos_html = []
        for produto in lista_produtos_card_html:
            lista_body_produtos_html.append(produto.find('div',class_='card-body'))
        lista_produtos = []
        for produto in lista_body_produtos_html:
            nome_produto = produto.find('h5',class_='card-title').get_text().strip()
            preco_produto = float(produto.find('p',class_='card-price').get_text().replace('Valor:','').replace('R$','').replace(',','.').strip())
            quantidade_produto = int(produto.find('p', attrs={'data-qtd':True}).get_text().replace('Disponível:','').replace('un.','').strip())
            lista_produtos.append(Produto(nome_produto, quantidade_produto, preco_produto))
    except Exception as ex:
        print(ex)
        exit()
    return lista_produtos

def buscar_produtos_site():
    html = acessar_url(URL)
    bs = retornar_html_parse(html)
    lista_produtos = obter_lista_produtos(bs)
    return lista_produtos