""" Calculadora com while"""


while True:
    entrada_primeiro_numero = input('Digite o primeiro numero: ')
    entrada_segundo_numero = input('Digite o segundo numero: ')
    entrada_operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    float_primeiro_numero = 0
    float_segundo_numero = 0

    try:
        float_primeiro_numero = float(entrada_primeiro_numero)
        float_segundo_numero = float(entrada_segundo_numero)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os numeros digitados são invalidos')
        continue

    operadores_permitidos = '+-/*'

    if entrada_operador not in operadores_permitidos:
        print('Operador invalido.')
        continue

    if len(entrada_operador) > 1:
        print('digite apenas um Operador.')
        continue

    if entrada_operador == '+':
        print(f'a soma dos numeros é:', float_primeiro_numero + float_segundo_numero)
    elif entrada_operador == '-' :
        print(f'a subitração dos numeros é:', float_primeiro_numero - float_segundo_numero)
    elif entrada_operador == '*':
        print(f'a multiplicação dos numeros é:', float_primeiro_numero * float_segundo_numero)
    elif entrada_operador == '/':
        print(f'a multiplicação dos numeros é:', float_primeiro_numero / float_segundo_numero)
    else:
        print('Não conheço esse operador')
              
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair == 's':
        break
