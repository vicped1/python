# variaveis são usadas para salvar algo na memoria do computador.
# PEP8: inicie variaveis com letras minusculas, pode usar
# numeros com underline
# o sinal de = e o operador de atribuição. ele e usado para
# atribuir um valor a um nome (variavel).
# Uso: nome_variavel = expressão

# nome_completo = 'Pedro Vitor Medeiros Holanda Pequeno'
# soma_dois_mais_dois = 2 + 2
# int_um = int('1')
# print(int_um, type(int_um))
# print(nome_completo, soma_dois_mais_dois) # Pedro Vitor Medeiros Holanda Pequeno
 
nome = "Pedro Vitor"
idade = 23
maior_de_idade = idade >= 18
if maior_de_idade == True:
    print("O" ,nome, "e maior de idade")
else:
    print("O", nome, "não e maior de idade")