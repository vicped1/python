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
lista_a = [1,2,3,4]
lista_b = [5,6,7,8]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
lista_c.reverse()
print(lista_c)
