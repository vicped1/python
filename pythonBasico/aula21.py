# Operadores logicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia 
# toda a expressão como verdadeiras.
# se qualquer valor for considerado verdadeiro,
# a expressão inteira sera avaliada naquele valor
# São consideradas falsy (que voce ja viu)
# 0 0.0 '' False
# também existe o tipo none que é
# usado para repersentar um não valor

# entrada = input('[E]ntrar [S]air: ')
# senha = input('digite a sua senha: ')

# senha_permitida = '1234'

# if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
#     print('Voce entrou no sistema')
# else:
#     print('Voce saiu do sistema')

# Avaliação de curto circuito
# print(True and True)
# print(True or False and True)
# print(bool(''))
# print(True and True and True)

senha = input('Senha: ') or 'Sem senha'
print(senha)