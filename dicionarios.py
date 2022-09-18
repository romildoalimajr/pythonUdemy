meu_dicionario = {'A': 'ameixa', 'B':'banana', 'C':'cajá', 'D': 'dendê'}

print(meu_dicionario)

for chave in meu_dicionario:
	print(chave)

for chave in meu_dicionario:
	print(meu_dicionario[chave])

for chave in meu_dicionario:
	print(chave + ' - ' + meu_dicionario[chave])

for item in meu_dicionario.items():
	print(item)

for valor in meu_dicionario.values():
	print(valor)

for chaves in meu_dicionario.keys():
	print(chaves)