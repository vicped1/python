# Desempacotamento em chamadas
# de metodos e funções
string = 'ABCD'
lista = ['Leopoldo', 'Eline', 'Pedro']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],#0
    #0
    ['Elaine', ],  #1
    #0       1       2
    ['Pedro', 'João', 'Carlos', ],  #2
]

# a,b,c = lista
# print(a,c)

# print(*string)
# print(*lista)
# print(*tupla)

print(*salas, sep='\n')
