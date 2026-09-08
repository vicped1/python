"""
CONSTANTES = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)
"""
velocidade = 61 # velocicdade atual do carro
local_carro = 100 # local em que o carro se encontra na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local em que o radar 1 se encontra na estrada
RADAR_RANGE = 1 # alcance do radar em metros

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE):
    if velocidade > RADAR_1:
        print('Você excedeu o limite de velocidade')
    else:
        print('Não foi multado')
else:
    print('Não está na área do radar')