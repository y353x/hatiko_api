import os

from django.core.management.base import BaseCommand
from dotenv import load_dotenv
from telebot import TeleBot
from api.requests import imei_check_request

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
IMEI_API_TOKEN = os.getenv('IMEI_API_TOKEN')


bot = TeleBot(TELEGRAM_TOKEN, threaded=False)
WHITE_LIST = (201951335,)


class Command(BaseCommand):

    @bot.message_handler(commands=['start'])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'На связи)')

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        if message.chat.id not in WHITE_LIST:
            bot.send_message(message.chat.id, 'not in white list')
        elif len(message.text) != 15:
            bot.send_message(message.chat.id, 'wrong imei length')
        else:
            imei = message.text
            try:
                check_result = imei_check_request(imei, IMEI_API_TOKEN)
                bot.send_message(message.chat.id,
                                 f'imei: {message.text}\n{check_result}')
            except BaseException:
                bot.send_message(
                    message.chat.id, 'ошибка по запросу: ' + message.text)

    def handle(self, *args, **kwargs):
        print('listening...')
        bot.infinity_polling()
