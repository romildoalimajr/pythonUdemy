arquivo = open('arquivo.txt')

linhas = arquivo.readlines()
print(linhas)

for linha in linhas:
	print(linha)

texto_completo = arquivo.read()
print(texto_completo)

w = open('arquivo2.txt', 'w')

w.write('Esse eh o meu arquivo de número 02')
w.close()