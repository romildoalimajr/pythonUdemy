import random

random.seed() #exibe o mesmo resultado
numero = random.randint(0,10)
print(numero)

lista = [6,45,9]

numero = random.choice(lista)
print(numero)

bicho = random.randint(0,9999)

print(bicho)

jogo_bicho = []

sorteio = 0

while sorteio < 5:
	resultado = random.randint(0,9999)
	jogo_bicho.append(resultado)
	print(resultado)
	sorteio += 1

print(jogo_bicho)
