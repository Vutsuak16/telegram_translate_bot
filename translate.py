__name__ = "vustuak"

from yandex_translate import YandexTranslate

from telegram import Updater

updater = Updater(token='182525986:AAEqN_dS1pPpjv4-9fuGLJEwptLEPEqjX6E')

dispatcher = updater.dispatcher


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Enter text/Language")


dispatcher.addTelegramCommandHandler('start', start)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="No such command")


dispatcher.addUnknownTelegramCommandHandler(unknown)


def Translate(bot, update, args):
    text = ""
    lang=""
    translate = YandexTranslate('trnsl.1.1.20160325T155459Z.530111cef80a4396.4bd3a5cce52a043929b86038587f3b22d6caa30f')
    for i in args:
        if i==args[-1]:
            text+=args[-1].split('/')[0]
            lang=args[-1].split('/')[1]
        else:
            text+=i+" "
    print text
    print lang
    bot.sendMessage(chat_id=update.message.chat_id, text="No such command")


dispatcher.addTelegramCommandHandler('Translate', Translate)

updater.start_polling()
