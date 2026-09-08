"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - Ìndices e fatiamento
Metodos úteis: 
    append: 
    insert: 
    pop:
    del:
    clear: 
    extend: 
    + - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3 
lista = [10, 20, 30, 40]
lista.append('Pedro')
nome = lista.pop()
lista.append(50)
del lista[-1]
# lista.clear()
lista.insert(0, 5)
print(lista)