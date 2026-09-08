"""
enumerate - enumera iteráveis (ìndices)
"""
# [(0, 'Pedro'), (1, 'Eline'), (2, 'Leopoldo'), (3, 'Maria')]
nomes = ['Pedro', 'Eline', 'Leopoldo']
nomes.append('Maria')

for indice, nome in enumerate(nomes):
    print(indice, nome)

# for i in enumerate(nomes):
#     indice, nome = i
#     print(indice, nome)

# for tupla_enumerada in enumerate(nomes):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')