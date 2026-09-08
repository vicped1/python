"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = "Pedro Vitor"
outra_variavel = f'{string[:4]}OOO{string[5:]}'
# string[4] = 'a'
print(string)
print(outra_variavel)
print(string.zfill(20))