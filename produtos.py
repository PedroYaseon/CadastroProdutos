listaProdutos = []
#Começo Cadastrar Produto
#Cadastro com dicionário e lista
def cadastrarProduto(codigo):
    print('Você selecionou a opção de Cadastrar Produto')
    print('Código do produto: {}' .format(codigo))
    nome = input('Digite o nome do Produto: ')
    fabricante = input('Digite o fabricante do Produto: ')
    valor = input('Digite o valor do Produto: ')
    dicionarioProduto = {'codigo'     : codigo,
                         'nome'       : nome,
                         'fabricante' : fabricante,
                         'valor'      : valor}
    listaProdutos.append(dicionarioProduto.copy())
#Fim Cadastrar Produto

#Começo Consultar Produto

def consultarProduto():
    #Função para consulta de produtos que pode ser de todos ou por categoria
    while True:
        try:
            print('Você selecionou a opção de Consultar Produto')
            opcConsultar = int(input('Escolha a opção desejada: \n1-Consultar Todos os Produtos \n2-Consultar Produto por Código '
                                     '\n3-Consultar Produtos por Fabricante\n4-Retornar \n>>'))
            if opcConsultar == 1:
                print('Todos os produtos disponíveis: ')
                for produto in listaProdutos:
                    for key, value in produto.items():
                        print('{} : {}' .format(key,value))
            elif opcConsultar == 2:
                ent = int(input('Digite o CÓDIGO do produto: '))
                for produto in listaProdutos:
                    if(produto['codigo'] == ent):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))
            elif opcConsultar == 3:
                ent = input('Digite o FABRICANTE do(s) produto(s): ')
                for produto in listaProdutos:
                    if(produto['fabricante'] == ent):
                        for key, value in produto.items():
                            print('{} : {}'.format(key, value))
            elif opcConsultar == 4:
                break
            else:
                print('Digite apenas as opções disponíveis')
        except ValueError:
            print('Digite apenas as opções disponíveis')


#Fim Consultar Produto

#Começo Remover Produto
#Função para remover o produto de acordo com o código

def removerProduto():
    print('Você selecionou a opção de Remover Produto')
    ent = int(input('Digite o CÓDIGO do produto: '))
    for produto in listaProdutos:
        if (produto['codigo'] == ent):
            listaProdutos.remove(produto)
#Fim Remover Produto

#Começo MAIN Produto

print('Bem vindo ao programa de produtos')

registroProduto = 0
while True:
    try:
        opcao = int(input('Escolha a opção desejada: \n1-Cadastrar Produto \n2-Consultar Produto \n3-Remover Produto \n4-Sair \n>>'))

        if opcao == 1:
            registroProduto = registroProduto + 1
            cadastrarProduto(registroProduto)
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            print('Programa Finalizado!')
            break
        else:
            print('Digite apenas as opções disponíveis')
            continue
    except ValueError:
        print('Digite apenas as opções disponíveis')


#Fim MAIN Produto
