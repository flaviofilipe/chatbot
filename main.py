from Chatbot import Chatbot

Bot = Chatbot("Filipe")
while True:
	frase = Bot.escuta()
	resp = Bot.pensa(frase)
	Bot.fala(resp)
	if resp == 'tchau':
		break;