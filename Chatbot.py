import json
import sys
import os
import subprocess as s


class Chatbot(object):
    """docstring for Chatbot"""

    def __init__(self, nome):
        try:
            memoria = open(nome + '.json', 'r')  # Abre o arquivo memoria para leitura
        except FileNotFoundError:
            memoria = open(nome + '.json', 'w')
            # Dicionario de Conhecidos e Frases
            memoria.write('[["Flavio","Filipe"],{"oi": "Olá, qual o seu nome?","tchau":"tchau"}]')
            memoria.close()
            memoria = open(nome + '.json', 'r')

        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)  # Carrega o arquivo memoria e armazena na lista de conhecidos
        memoria.close()
        self.historico = [None]

    def escuta(self, frase=None):
        # frase = arg opcional
        if (frase == None):
            frase = input('>:')
        frase = str(frase)
        if 'executa' in frase:
            return frase
        frase = frase.lower()  # tudo minuscula
        frase = frase.replace('é', 'e')  # substitui
        return frase

    def pensa(self, frase):
        # Pesquisar frase no dicionario
        if frase in self.frases:
            return self.frases[frase]

        if frase == 'aprende':
            return 'Digite a frase: '

        #Responde frases que dependem do historico
        ultimaFrase = self.historico[-1]
        if ultimaFrase == 'Olá, qual o seu nome?':  # Verifica ultima frase do historico
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase
        if(ultimaFrase == 'Digite a frase: '):
            self.chave = frase
            return 'Digite a resposta: '
        if(ultimaFrase == 'Digite a resposta: '):
            resp = frase
            self.frases[self.chave] = resp
            self.gravaMemoria()
            return 'Aprendido'

        try:
            resp = str(eval(frase))  # Converte para String
            return resp
        except:
            pass
        return 'Não Entendi'

    def pegaNome(self, nome):
        if 'o meu nome e ' in nome:
            # Pega apartir da posicao 13
            nome = nome[13:]
        # primeiras letras em maiusculo
        nome = nome.title()
        return nome

    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = 'Eaew '
        else:
            frase = 'Muito Prazer '
            # Sempre que conhece pessoa armazena nome na lista de conhecidos
            self.conhecidos.append(nome)
            self.gravaMemoria()

        return frase + nome

    def gravaMemoria(self):
        memoria = open(self.nome + '.json', 'w')
        json.dump([self.conhecidos, self.frases], memoria)  # Escreve no arquivo memoria a lista de conhecidos
        memoria.close()

    def fala(self, frase):
        if 'executa ' in frase:
            plataforma = sys.platform
            comando = frase.replace('executa ', '')  # Deleta o nome executa
            if 'win' in plataforma:
                os.startfile(comando)
                print(frase)
            if 'linux' in plataforma:
                try:
                    s.Popen(comando)
                except FileNotFoundError as e:
                    s.Popen(['xdg-open', comando])
        else:
            print(frase)
        self.historico.append(frase)  # Inclui frase no historico
