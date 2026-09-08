"""
cuidado com dados mutaveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor n memoria (mutavel)
"""
# nome = 'Pedro'
# outra_variavel = nome
# nome = 'Eline'
# print(nome)
# print(outra_variavel)

lista = ['Pedro', 'Eline', 1, True, 1.2]
lista2 = lista.copy()

lista[0] = 'Leopoldo'
print(lista)
print(lista2)
