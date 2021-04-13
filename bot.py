import telebot
import config  # BOT_TOKEN token got from FatherBot
import content_messages
import checks
import re
from threading import Thread

bot = telebot.TeleBot(config.BOT_TOKEN)
chat_id = 0
count = 0
links = ""
chats_id = []


# fSticker = open("sources/F.webp", 'rb')

def counter():
    global count
    count += 1
    return count

def threadingTester():
    while():
        text = str(input())
        if(text != "!quit"):
            for id in chats_id:
                bot.send_message(
                    id, text
                )
        else:
            break




def switchText(text):
    layout_to_rus = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                                      'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                             "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                             'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))
    text = str(text)
    if (re.search(r'[а-яА-ЯёЁ]', text)):
        layout_to_eng = dict(zip(map(ord, "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                                          'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'),
                                 "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                                 'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'))
        return (text.translate(layout_to_eng))
    return (text.translate(layout_to_rus))


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     content_messages.START_TEXT,
                     parse_mode='markdown')
    if message.chat.id not in chats_id:
        chats_id.append(message.chat.id)
    # chat_id = message.chat.id


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
    checks.triggerCheck(message, bot)
    print(message.chat.id)


@bot.message_handler(content_types=['photo'])
def forwall(message):
    print(str(message) + '\n' + 'ATTENTION!!! IMAGE ')


print("Bot was started, waiting for a dialog")


botThread = Thread(target=bot.polling, args=({"none_stop": True},))

botThread.start()
adminBackThread = Thread(target=threadingTester, args=())
adminBackThread.start()
# bot.polling(none_stop=True)
