def menu_atendimento():
    print('''
    ==============================
    =  Menu de Caixa Atendimento =
    ==============================
    = 1 - Iniciar Atendimento    =
    ------------------------------
    = 2 - Finalizar Atendimentos =
    ==============================
    ''')

def menu_compra():
    print('''
    ==============================
    =      Menu de Compra        =
    ==============================
    = 1 - Adicionar Produto      =
    ------------------------------
    = 2 - Finalizar Compra       =
    ==============================
    ''')

def menu_administracao():
    print('''
    ==============================
    =   Menu Administração SIG   =
    ==============================
    = 0 - Visualizar MENU        =
    ------------------------------
    = 1 - Adm. Produto           =
    ------------------------------
    = 2 - Adm. Cliente           =
    ------------------------------
    = 3 - Adm. Fornecedor        =
    ------------------------------
    = 4 - Resetar Banco de Dados =
    ------------------------------
    = 5 - Sair do Sistema ADM    =
    ==============================
    ''')

def menu_administracao_produto():
    print('''
    ==============================
    =      Menu Adm. Produto     =
    ==============================
    = 0 - Visualizar MENU        =
    ------------------------------
    = 1 - Adm. CRUD Dados        =
    ------------------------------
    = 2 - Consultar Dados        =
    ------------------------------
    = 3 - Sair ADM Produto       =
    ==============================
    ''')

def menu_produto_CRUD():
    print('''
    ==============================
    =      Menu CRUD Produto     =
    ==============================
    = 0 - Visualizar MENU        =
    ------------------------------
    = 1 - Visualizar Produtos    =
    ------------------------------
    = 2 - Visualizar Um Produto  =
    ------------------------------
    = 3 - Adicionar Produto      =
    ------------------------------
    = 4 - Modificar Produto      =
    ------------------------------
    = 5 - Deletar Produto        =
    ------------------------------
    = 6 - Resetar Dados Produto  =
    ------------------------------
    = 7 - Sair CRUD Produto      =
    ==============================
    ''')

def menu_produto_consultas():
    print('''
    ==============================
    =   Menu Consultas Produto   =
    ==============================
    = 0 - Visualizar MENU        =
    ------------------------------
    = 1 - Mais Vendidos          =
    ------------------------------
    = 2 - Menos Vendidos         =
    ------------------------------
    = 3 - Pouco Estoque          =
    ------------------------------
    = 4 - Exibir Fornecedores    =
    ------------------------------
    = 5 - Sem Fornecedores       =
    ------------------------------
    = 6 - Sair Consulta Produto  =
    ==============================
    ''')

def menu_modificar_produto():
    print('''
    ==============================
    =     Menu de Modificação    =
    ==============================
    = 1 - Modificar Preço        =
    ------------------------------
    = 2 - Modificar Quantidade   =
    ------------------------------
    = 3 - Sair Opção Modificação =
    ==============================
    ''')

def menu_administracao_cliente():
    print('''
    ==============================
    =      Menu Adm. Cliente     =
    ==============================
    = 0 - Visualizar MENU        =
    ------------------------------
    = 1 - Adm. CRUD Dados        =
    ------------------------------
    = 2 - Consultar Dados        =
    ------------------------------
    = 3 - Sair ADM Cliente       =
    ==============================
    ''')

def menu_cliente_CRUD():
    print('''
    ==============================
    =      Menu CRUD Cliente     =
    ==============================
    = 0 - Visualizar MENU        =
    ------------------------------
    = 1 - Visualizar Clientes    =
    ------------------------------
    = 2 - Visualizar Um Cliente  =
    ------------------------------
    = 3 - Resetar Dados Cliente  =
    ------------------------------
    = 4 - Sair CRUD Cliente      =
    ==============================
    ''')

def menu_cliente_consultas():
    print('''
    ==============================
    =   Menu Consultas Cliente   =
    ==============================
    = 0 - Visualizar MENU        =
    ------------------------------
    = 1 - Clientes Com Compras   =
    ------------------------------
    = 2 - Clientes Sem Compras   =
    ------------------------------
    = 3 - Compras Um Cliente     =
    ------------------------------
    = 4 - Info Compra De Cliente =
    ------------------------------
    = 5 - Clientes c/Mais Compras=
    ------------------------------
    = 6 - Clientes c/Mais Gasto  =
    ------------------------------
    = 7 - Sair Consulta Cliente  =
    ==============================
    ''')

def menu_administracao_fornecedor():
    print('''
    ==============================
    =     Menu Adm. Fornecedor   =
    ==============================
    = 0 - Visualizar MENU        =
    ------------------------------
    = 1 - Adm. CRUD Dados        =
    ------------------------------
    = 2 - Consultar Dados        =
    ------------------------------
    = 3 - Sair ADM Fornecedor    =
    ==============================
    ''')

def menu_fornecedor_CRUD():
    print('''
    ==============================
    =     Menu CRUD Fornecedor   =
    ==============================
    = 0 - Visualizar MENU        =
    ------------------------------
    = 1 - Visualizar Fornecedores=
    ------------------------------
    = 2 - Visualizar Um Fornec.  =
    ------------------------------
    = 3 - Adicionar Fornecedor   =
    ------------------------------
    = 4 - Modificar Fornecedor   =
    ------------------------------
    = 5 - Deletar Fornecedor     =
    ------------------------------
    = 6 - Resetar Dados Fornec.  =
    ------------------------------
    = 7 - Sair CRUD Fornecedor   =
    ==============================
    ''')

def menu_modificar_fornecedor():
    print('''
    =================================
    =       Menu de Modificação     =
    =================================
    = 1 - Adicionar Fornec. de Prod.=
    ---------------------------------
    = 2 - Retirar Fornec. de Prod.  =
    ---------------------------------
    = 3 - Sair Opção Modificação    =
    =================================
    ''')

def menu_fornecedor_consultas():
    print('''
    ==============================
    =  Menu Consultas Fornecedor =
    ==============================
    = 0 - Visualizar MENU        =
    ------------------------------
    = 1 - Fornecedores C/ Prod.  =
    ------------------------------
    = 2 - Fornecedores S/ Prod.  =
    ------------------------------
    = 3 - Prod. de um Fornecedor =
    ------------------------------
    = 4 - Sair Consulta Fornec.  =
    ==============================
    ''')