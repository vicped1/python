"""
exercicio
peça ao usuario para digitar seu nome
peça ao usuario para digitar sua idade
Se nome e idade forem digitados:
    exiba:
        seu nome é {nome}
        seu nome invertido é {nome invertido}
        seu nome contem (ou não) espaços
        seu nome tem {qtd} letras
        a primeira letra do seu nome é {letra}
        a ultima letra do seu nome é {letra}
se nome ou idade não forem digitados:
    exiba:
        Desculpe, você deixou campos vazios.
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')