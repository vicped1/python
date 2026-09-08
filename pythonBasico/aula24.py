"""
interpolação basica de strings
s - string
d e i - int
f - float
x e X - hexadecimais (ABCDEF0123456789)
"""
nome = 'Pedro Vitor'
preco = 1000.958976
variavel = f'%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %08x' % (1500, 1500))