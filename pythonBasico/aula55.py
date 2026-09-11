"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
lista_de_compras = []
produto = input('Digite "inserir" para adicionar um produto, "listar" para ver a lista, "apagar" para remover um item ou "sair" para encerrar: ')
while produto != 'sair':
    if produto == 'listar':
        for indice, produto in enumerate(lista_de_compras):
            print(indice, produto)
    elif produto == 'apagar':
        indice = int(input('Digite o índice do produto que deseja apagar: ')) 
        try:
            lista_de_compras.pop(indice)
        except IndexError:
            print('Índice inválido.')
    elif produto == 'inserir':
        produto = input('Digite um produto: ')
        lista_de_compras.append(produto)
    produto = input('Digite "inserir" para adicionar um produto, "listar" para ver a lista, "apagar" para remover um item ou "sair" para encerrar: ')