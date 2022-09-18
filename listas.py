minha_lista = ['abacaxi', 'melancia', 'abacate']
minha_lista2 = [1,2,3,4,5,6,7,8,9,10]
minha_lista3 = ["abacaxi", 2, 9.98, True]


tamanho = len(minha_lista2)

print(tamanho)
print(minha_lista[2])

print(minha_lista)
print(minha_lista2)
print(minha_lista3)

for item in minha_lista:
	print(item)

minha_lista.append("carambola")

print(minha_lista)

if 7 in minha_lista2:
	print('7 está na lista')

del minha_lista[2:]

print(minha_lista)

del minha_lista[:]

print(minha_lista)

minha_lista4 = []

minha_lista4.append(99)
print(minha_lista4)