primeiro_valor = input('digite um valor: ')
segundo_valor = input('digite outro valor: ')

# primeiro_valor_inteiro = int(primeiro_valor)
# segundo_valor_inteiro = int(segundo_valor)

if primeiro_valor >= segundo_valor:
    print(f'o {primeiro_valor=} é maior ou igual que o {segundo_valor=}')
elif primeiro_valor < segundo_valor:
    print(f'o {segundo_valor=} é maior que o {primeiro_valor=}')
else:
    print('digite apenas numeros')
