"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quando um codigo não tem fim
"""
contador = 0

while contador < 100:
    contador += 1

    if contador == 10:
        print('Não vou mostrar o 10')
        continue 

    if contador >= 11 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue 

    print(contador)

    if contador == 40:
        break


print('Acabou')