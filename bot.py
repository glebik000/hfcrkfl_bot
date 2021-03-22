import telebot
import config  # BOT_TOKEN token got from FatherBot
import content_messages
import re

bot = telebot.TeleBot(config.BOT_TOKEN)
chat_id = 0
count = 0
links = ""

#fSticker = open("sources/F.webp", 'rb')


def counter():
    global count
    count += 1
    return count


def pidorCheck(message):
    msg = message.text
    if ("пидор" in msg.lower()):
        bot.send_message(message.chat.id, "@" + str(message.from_user.username) + ", cам пидор",
                         reply_to_message_id=message.id)
    else:
        print(message.text)


def pizdaCheck(message):
    msg = message.text
    if ("да" == msg.lower()):
        bot.send_message(message.chat.id, "ПИЗДА", reply_to_message_id=message.id)


def noCheck(message):
    msg = message.text
    if ("нет" == msg.lower() or "нет." == msg.lower()):
        bot.send_message(message.chat.id, "Пидора ответ",
                         reply_to_message_id=message.id)


def fCheck(message):
    msg = message.text
    if ("f" == msg.lower()) or ("press f" == msg.lower()):
        fSticker = open("sources/F.webp", 'rb')
        if message.reply_to_message:
            bot.send_sticker(
                message.chat.id,
                fSticker,
                reply_to_message_id=message.reply_to_message.id
            )
        else:
            bot.send_sticker(message.chat.id, fSticker)


def switchText(text):
    layout_to_rus = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                                      'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                             "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                             'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))
    text = str(text)
    if(re.search(r'[а-яА-ЯёЁ]', text)):
        layout_to_eng = dict(zip(map(ord, "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                                          'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'),
                                 "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                                 'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'))
        return (text.translate(layout_to_eng))
    return (text.translate(layout_to_rus))


def triggerCheck(message):
    pidorCheck(message)
    pizdaCheck(message)
    fCheck(message)
    noCheck(message)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     content_messages.START_TEXT,
                     parse_mode='markdown')
    chat_id = message.chat.id


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     content_messages.HELP_TEXT)


@bot.message_handler(commands=['pleh'])
def pleh(message):
    bot.send_message(message.chat.id,
                     "PLEH COMING SOON...")


@bot.message_handler(commands=['switch'])
def switch(message):
    if message.reply_to_message.content_type == 'text':
        if message.reply_to_message:
            bot.send_message(
                message.chat.id,
                switchText(message.reply_to_message.text),
                reply_to_message_id=message.reply_to_message.id
            )
        else:
            bot.send_message(
                message.chat.id, "Please reply on the TEXT message.", reply_to_message_id=message.id
            )
    if message.reply_to_message.content_type != 'text':
        if message.reply_to_message:
            bot.send_message(
                message.chat.id,
                switchText(message.reply_to_message.caption),
                reply_to_message_id=message.reply_to_message.id
            )
        else:
            bot.send_message(
                message.chat.id, "Please reply on the TEXT message.", reply_to_message_id=message.id
            )
        print(message.reply_to_message.caption)

@bot.message_handler(commands=['howmuchmessages'])
def countmsgs(message):
    counts = counter()
    bot.send_message(message.chat.id, str(counts))
    print(counts)


@bot.message_handler(content_types=['text'])
def forwarding(message):
    print(message)
    triggerCheck(message)
    print(message.chat.id)

@bot.message_handler(content_types=['photo'])
def forwall(message):
    print(str(message) + '\n' + 'ATTENTION!!! IMAGE ')

print("Bot was started, waiting for a dialog")
bot.polling(none_stop=True)
