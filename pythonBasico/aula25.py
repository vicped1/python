"""
Formatação basica de strings
S - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
sinal - + ou -
ex.: 0>-100,.1f
conversaion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.487368123746:0=+10,.1f}')
print(f'o hexadecimal de 1500 é {1500:08X}')