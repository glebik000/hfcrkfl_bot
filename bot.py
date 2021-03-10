import telebot
import config  # BOT_TOKEN token got from FatherBot
import content_messages

bot = telebot.TeleBot(config.BOT_TOKEN)
chat_id = 0
count = 0
links = ""


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
    if ("да" in msg.lower()):
        bot.send_message(message.chat.id, "ПИЗДА", reply_to_message_id=message.id)
    else:
        print(message.text)


def switchText(text):
    layout = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                               'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                      "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                      'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))
    return (text.translate(layout))


def triggerCheck(message):
    pidorCheck(message)
    pizdaCheck(message)


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
    bot.send_message(
        message.chat.id,
        switchText(message.reply_to_message.text),
        reply_to_message_id=message.reply_to_message.id
    )


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


print("Bot was started, waiting for a dialog")
bot.polling(none_stop=True)
