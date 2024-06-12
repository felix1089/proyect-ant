import telebot

TOKEN = '7326279593:AAEvFOJCeSF3qkNRkCRK8jyYSMKHAEl78PM'

bot = telebot.TeleBot(TOKEN)
#print(bot)

@bot.message_handler(commands=['start'])
def star_welcome(message):
    bot.reply_to(message, 'Welcomen ant game')
    #print(star_welcome)
    
    
    
@bot.message_handler(commands=['start'])
def send_help(message):
    bot.reply_to(message, "option solo por ahora nada /start")
#print(send_help)


@bot.message_handler(func=lambda m: True)
def echoll_all(message):
    bot.reply_to(message, message.text)
   ## print(echoll_all)
    

if __name__ == "bot.py":
    bot.polling(none_stop=True)





    