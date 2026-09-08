"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - Ìndices e fatiamento
Metodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
import os
import subprocess
subprocess.run(['clear' if os.name == 'posix' else 'cls'], shell=(os.name != 'posix'))
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'removido,', ultimo_valor)
