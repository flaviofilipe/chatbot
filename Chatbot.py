import json

class Chatbot(object):
	"""docstring for Chatbot"""
	def __init__(self, nome):
		try:
			memoria = open(nome+'.json','r') #Abre o arquivo memoria para leitura
		except FileNotFoundError:
			memoria = open(nome+'.json', 'w')
			memoria.write('["Flavio","Filipe"]')
			memoria.close()
			memoria = open(nome+'.json','r')
		self.nome = nome
		self.conhecidos = json.load(memoria) #Carrega o arquivo memoria e armazena na lista de conhecidos
		memoria.close()
		self.historico = [ ]

		#Dicionario de frases
		self.frases = {
		'oi': 'Olá, qual o seu nome?',
		'tchau':'tchau'
		} 
	
	def escuta(self):
		frase = input ('>:')
		frase = frase.lower() #tudo minuscula
		frase = frase.replace('é','e') #substitui
		return frase

	def pensa(self, frase):
		#Pesquisar frase no dicionario
		if frase in self.frases:
			return self.frases[frase]
		if frase == 'aprende':
			chave 	= input('Digite a frase: ')
			resp 	= input('Digite a resposta: ')
			self.frases[chave] = resp
			return 'Aprendido'

		if self.historico[-1] == 'Olá, qual o seu nome?': #Verifica ultima frase do historico
			nome = self.pegaNome(frase)
			resp = self.respondeNome(nome)
			return resp

		try:
			resp = eval(frase)
			return resp
		except:
			pass
		return 'Não Entendi'

	def pegaNome(self, nome):
		if 'o meu nome e ' in nome:
			#Pega apartir da posicao 13
			nome = nome[13:]
		#primeiras letras em maiusculo
		nome = nome.title()
		return nome

	def respondeNome(self, nome):
		if nome in self.conhecidos:
			frase = 'Eaew '
		else:
			frase = 'Muito Prazer '
			#Sempre que conhece pessoa armazena nome na lista de conhecidos
			self.conhecidos.append(nome)
			memoria = open(self.nome+'.json', 'w')
			json.dump(self.conhecidos,memoria) #Escreve no arquivo memoria a lista de conhecidos
			memoria.close()

		return frase+nome

	def fala(self, frase):
		print (frase)
		self.historico.append(frase) #Inclui frase no historico

		