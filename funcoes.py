def resposta():
	#Pega resposta do usuario
	resp = input ('>:')
	resp = resp.lower() #tudo minuscula
	resp = resp.replace('é','e') #substitui
	return resp

def pegaNome(nome):
	if 'o meu nome e ' in nome:
		#Pega apartir da posicao 13
		nome = nome[13:]
	#primeiras letras em maiusculo
	nome = nome.title()
	return nome

def respondeNome(nome):
	conhecidos = ['Flavio','Filipe']
	if nome in conhecidos:
		frase = 'Eaew '
	else:
		frase = 'Muito Prazer '
	return frase+nome
