"""
Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se o numero é par ou inpar. caso o usuario não digite um numero
inteiro, informe que não é um numero inteiro.
"""

numero_inteiro = input('Digite um numero inteiro: ')

if numero_inteiro.isdigit():
    numero = int(numero_inteiro)
    par_ou_impar = (numero % 2 == 0)
    if par_ou_impar:
        print('O numero é par.')
    else:
        print('O numero é impar.')
else:
    print('O valor digitado não é um numero inteiro.')