n1 = int(input('Digite o primeiro número.: '))
sinal = input('Digite o sinal da operação.: ')
n2 = int(input('Digite o segundo número.: '))

if sinal == '+':
	op = n1 + n2
elif sinal == '-':
	op = n1 - n2
elif sinal == '*':
	op = n1 * n2
elif  sinal == '/':
	op = n1 / n2
else:
	print('Sinal inválido!!! :(')

print('O valor da operação de ' + n1 + sinal + n2 + ' = ' + op)