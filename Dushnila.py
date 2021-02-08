import telebot
bot = telebot.TeleBot('1609638154:AAENYpbHBfiPstRajZczhIth9pQ1x0DESXM')

@bot.message_handler(commands=['start']
               def send_welcome(message):
                   bot.reply_to(message, 'Здравствуй. Я помогу найти душнилу в чате')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

bot.polling(none_stop=True)

