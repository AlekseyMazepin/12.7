import telebot
from confing import keys, TOKEN
from extensions import APIException, CryptoConverter
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валты> \ <в какую валюту перевести> \ <количесмтво переводимой валюты>\nУвидить список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['stop'])
def help(message: telebot.types.Message):
    text = 'Всего хорошего, спасибо, что исользваоли нашего бота'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
       text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) != 3:
            raise APIException('Слишком много параметров')

        guote, base, amount = values
        total_base = CryptoConverter.convert(guote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text = f'Цена {amount} {guote} в {base} - {float(total_base) * float(amount)} {base}'
        bot.send_message(message.chat.id, text)


bot.polling()