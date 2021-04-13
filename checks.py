

def pidorCheck(message, bot):
    msg = message.text
    if ("пидор" in msg.lower()):
        bot.send_message(message.chat.id, "@" + str(message.from_user.username) + ", cам пидор",
                         reply_to_message_id=message.id)
    else:
        print(message.text)


def pizdaCheck(message, bot):
    msg = message.text
    if ("да" == msg.lower()):
        bot.send_message(message.chat.id, "ПИЗДА", reply_to_message_id=message.id)


def noCheck(message, bot):
    msg = message.text
    if ("нет" == msg.lower() or "нет." == msg.lower()):
        bot.send_message(message.chat.id, "Пидора ответ",
                         reply_to_message_id=message.id)


def fCheck(message, bot):
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

def triggerCheck(message, bot):
    pidorCheck(message, bot)
    pizdaCheck(message, bot)
    fCheck(message, bot)
    noCheck(message, bot)