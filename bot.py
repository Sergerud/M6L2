import os
import telebot
import base64
from config import TOKEN
from logic import FusionBrainAPI 
from PIL import Image

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет!")



@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Отправьте мне фото, и я размою лица на нем.")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    x=message.text
    api = FusionBrainAPI('https://api-key.fusionbrain.ai/', '', '')
    pipeline_id = api.get_pipeline()
    uuid = api.generate(x, pipeline_id)
    files = api.check_generation(uuid)[0]
    api.save_img(files, 'gen_foto.png')

    with open('gen_foto.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo) 
    #bot.reply_to(message, message.text)

if __name__ == "__main__":

    bot.polling(none_stop=True)
