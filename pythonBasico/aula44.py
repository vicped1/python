"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o preximo valor
iter -> me entregue seu iterador
"""
texto = iter('pedro') # iterável

# iterador = iter(texto)# iterator

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)