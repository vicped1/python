"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um codigo não tem fim
"""
# contador = 0
# while contador <= 10:
#     print(contador)
#     contador += 1
# print('fora do while')

condicao = True

while condicao:
    nome = input('Qual o seu nome? ')
    if nome == 'sair':
        condicao = False
    else:
        print(f'Olá {nome}')