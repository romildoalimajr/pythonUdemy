# função enumerate

lista = ['abacate', 'bola', 'cachorro']

for i in lista:
	print(i)

for i in range(len(lista)):
	print(i, lista[i])

# função enumerate sendo utilizada

for i, nome in enumerate(lista):
	print(i, nome)
