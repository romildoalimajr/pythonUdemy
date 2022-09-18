# função MAP

def dobro(x):
	return x * 2

valor = 2
print(dobro(valor))

valor = [1, 2, 3, 4, 5, 6, 7]


# aplicando a função MAP
valor_dobrado = (map(dobro, valor))

valor_dobrado = list(valor_dobrado)

print(valor_dobrado)
