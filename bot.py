import telebot
import config #BOT_TOKEN token got from FatherBot
import content_messages

bot = telebot.TeleBot(config.BOT_TOKEN)
chat_id = 0
count = 0

def counter():
    global count
    count += 1
    return count

def pidorCheck(message):
    msg = message.text
    if ("пидор" in msg.lower()):
        #bot.reply_to_message(message.chat.id, message.id,"Сам пидор")
        bot.send_message(message.chat.id, "@"+str(message.from_user.username)+", cам пидор", reply_to_message_id = message.id)
    else:
        #bot.send_message(message.chat.id, message.text)
        print(message.text)

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

@bot.message_handler(commands=['howmuchmessages'])
def countmsgs(message):

    counts = counter()
    bot.send_message(message.chat.id, str(counts))
    print(counts)

@bot.message_handler(content_types=['text'])
def forwarding(message):
    print(message)
    pidorCheck(message)
    print(message.chat.id)

print("Bot was started, waiting for a dialog")
bot.polling(none_stop=True)

