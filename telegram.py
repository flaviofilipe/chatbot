import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("429120534:AAHJLN3JpsuFOqrBGI91tuUFXPTNxcbWK98")
bot = Chatbot("Fx2")


def recebendoMsg(msg):
    frase = bot.escuta(frase=msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)
    # chatID = msg['chat']['id'] #id é um dicionario dentro de chat
    tipoMsg, tipoChat, chatID = telepot.glance(msg)  # Recebe lista e atribui as variaveis
    telegram.sendMessage(chatID, resp)


telegram.message_loop(recebendoMsg)

while True:
    pass
