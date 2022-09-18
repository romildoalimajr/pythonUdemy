a = 'Romildo'
b = 'Alves'

print(a)
print(b)

concatenar = a + ' ' + b + ' '

print(concatenar)

tamanho = len(concatenar)

print(tamanho)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])

print(concatenar[0:3])
print(concatenar.lower())
print(concatenar.upper())

print(concatenar.strip()) #remove espaços e caracteres especiais desnecessários

minha_string = 'O rato roeu a roupa do rei de Roma'

busca = minha_string.find('rei')
print(busca)
print(minha_string[busca:])

print(minha_string.replace('do rei','da rainha'))



minha_lista = minha_string.split()
print(minha_lista)

minha_lista = minha_string.split('r')
print(minha_lista)