"""
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - Ìndices e fatiamento
Metodos úteis: append, insert, pop, del, clear, extend, +
"""
import os
import subprocess
#         01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)
# print(bool([])) # falsy
# print(lista, type(lista))

#        0    1     2              3    4
#       -5   -4    -3             -2   -1
lista = [123, True, 'Pedro Vitor', 1.2, []]
subprocess.run(['clear' if os.name == 'posix' else 'cls'], shell=(os.name != 'posix'))
lista[-3] = 'Eline'
print(lista)
print(lista[2], type(lista[2]))
