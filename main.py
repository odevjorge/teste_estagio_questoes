# Questão 1: 91

# Questão 2: 
num = int(input("Digite um numero: "))

atual = 0
proximo = 1

resp = 'Não Faz Parte'
while atual < num:
    guardar = atual + proximo
    atual = proximo
    proximo = guardar

    if atual == num:
      resp = 'Faz Parte'

print(resp)

# Questão 3
# A) 9
# B) 128
# C) 49
# D) 100
# E) 13
# F) ?

"""
calculando o tempo de viagem que levaria
Caminhão 100/80 = 1.25h 
O tempo do caminhão é diferente por conta dos pedagios
1.25 + (10/60) = ~1.42h
100/1.42 = 70.6km/h

calculando distancia do caminhão em relação a 
distancia x velocidade do carro
110 * 100 / 110 + 70.6 = 60,9Km

Questão 4: 60,9Km
"""


# Questão 5:

texto = list(str(input("Digite um texto: ")))

for c in texto[::-1]:
  print(c, end='')