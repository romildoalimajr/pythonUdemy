# função ZIP

lista1 = [1,2,3,4,5]
lista2 = ['abacate', 'bola', 'cachorro', 'dinheiro', 'elefante']
lista3 = [2.00, 5.49, 4.75, 1698.39, 9999.89]
#utilizando a função ZIP

for numero, nome in zip(lista1, lista2):
	print(numero, nome)

for numero, nome, valor in zip(lista1, lista2, lista3):
	print(numero, nome, valor )