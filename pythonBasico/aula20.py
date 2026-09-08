# Operadores logicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser 
# verdadeiras.
# se qualquer valor for considerado falso,
# a expressão inteira sera avaliada naquele valor
# São consideradas falsy (que voce ja viu)
# 0 0.0 '' False
# também existe o tipo none que é
# usado para repersentar um não valor
# entrada = input('[E]ntrar [S]air: ')
# senha = input('digite a sua senha: ')

# senha_permitida = '1234'

# if entrada == 'E' and senha == senha_permitida:
#     print('Voce entrou no sistema')
# else:
#     print('Voce saiu do sistema')

# Avaliação de curto circuito
print(True and True)
print(True and False and True)
print(bool(''))
print(True and True and True)