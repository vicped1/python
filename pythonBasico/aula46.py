"""
Faça um jogo para o usuario adivinhar qual a palavra secreta.
- Voce vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuario digitar apenas uma letra.
- Quando o usuario digitar uma letra, voce vai conferir se a letra digitada esta na palavra secreta.
    - se a letra digitada estiver na palavra secreta; exiba a letra;
    - se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuario 
"""

import os
import subprocess


palavra_secreta = 'perfume'
contador = 0
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ')
    contador += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        subprocess.run(['clear' if os.name == 'posix' else 'cls'], shell=(os.name != 'posix'))
        print(f'Parabems voce ganhou!')
        print(f'a palavra secreta era {palavra_secreta}')
        print(f'voce levou {contador} tentativas para acertar a palavra secreta')
        palavra_formada = ''
        contador = 0
        letras_acertadas = ''
        sair_do_programa = input('voce deseja sair do programa? (s para sim e n para não) ')
        if sair_do_programa == 's':
            break

 
        
