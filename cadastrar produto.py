listadeprodutos = []
#--------------COMEÇO cadastrarProduto--------------#
def cadastrarProduto(rp):
    print('Bem-vindo ao Cadastrar Produto')
    print('O RP do produto a ser cadastrado é: {}'.format(rp))
    nome = input('Digite o nome do produto: ')
    fabricante = input('Digite o fabricante do produto: ')
    valor = input('Digite o valor do produto: ')
    dicionarioProduto = {'rp'         : rp,
                         'fabricante' : fabricante,
                         'nome'       : nome,
                         'valor'      : valor}
    listadeprodutos.append(dicionarioProduto.copy())
#--------------FIM cadastrarProduto-----------------#


#--------------COMEÇO consultarProduto--------------#
def consultarProduto():
    while True:
        try:
            print('Bem-vindo ao Consultar Produto')
            opConsultar = int(input('Entre com a opção desejada:\n1-Consultar todos os produtos\n2-Consultar produtos por codigo\n3-Consultar por fabricante\n4-Retornar\n>>'))
            if opConsultar == 1:
                print('Bem-vindo a consultar todos')
                for produto in listadeprodutos:
                    for key, value in produto.items():
                        print("{} : {}".format(key,value))
            elif opConsultar == 2:
                print('Bem-Vindo a consultar produtos por codigo')
                entrada = int(input('Digite o RP desejado: '))
                for produto in listadeprodutos:
                    if(produto['rp'] == entrada):
                        for key, value in produto.items():
                            print("{} : {}".format(key,value))
            elif opConsultar == 3:
                print('Bem-Vindo a consultar produtos por fabricante')
                entrada = input('Digite o fabricante desejado: ')
                for produto in listadeprodutos:
                    if (produto['fabricante'] == entrada):
                        for key, value in produto.items():
                            print("{} : {}".format(key, value))
            elif opConsultar == 4:
                return
            else:
                print('Pare de digitar números que não existem no menu')
        except ValueError:
            print('Pare de digitar valores não inteiros')
#--------------FIM consultarProduto-----------------#


#--------------COMEÇO removerProduto----------------#
def removerProduto():
    print ('Bem-vindo ao Remover Produto')
    entrada = int(input('Digite o RP desejado: '))
    for produto in listadeprodutos:
        if (produto['rp'] == entrada):
            listadeprodutos.remove(produto)
#--------------FIM removerProduto-------------------#


#--------------COMEÇO MAIN--------------------------#
print('Bem-vindo ao Controle de Estoque do Victor Akio Obu')
registroProduto = 0
while True:
    try:
        opcao = int (input("Digite a opção desejada:\n1-Cadastrar Produto\n2-Consultar Produto\n3-Remover Produto\n4-Sair\n>>"))
        if opcao == 1:
            registroProduto = registroProduto + 1
            cadastrarProduto(registroProduto)
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            print('Programa finalizado')
            break
        else:
            print('Pare de digitar números que não existem no menu')
            continue
    except ValueError:
        print('Pare de digitar valores não inteiros')
#--------------FIM MAIN-----------------------------#
