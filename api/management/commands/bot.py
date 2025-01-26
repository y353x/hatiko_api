import os
import re

from django.core.management.base import BaseCommand
from dotenv import load_dotenv
from telebot import TeleBot

from api.constants import IMEI_REGEX
from api.requests import imei_check_request

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
IMEI_API_TOKEN = os.getenv('IMEI_API_TOKEN')
WHITE_LIST = [int(_) for _ in os.getenv('WHITE_LIST').split(',')]


bot = TeleBot(TELEGRAM_TOKEN, threaded=False)


class Command(BaseCommand):

    @bot.message_handler(commands=['start'])
    def start(m, res=False):
        bot.send_message(m.chat.id, 'Alive)')

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        text = message.text
        if message.chat.id not in WHITE_LIST:
            error = 'Not in white list'
            bot.send_message(message.chat.id, error)
        elif not re.match(IMEI_REGEX, str(text)):
            error = 'Wrong imei. Should contain 15 digits only'
            bot.send_message(message.chat.id, error)
        else:
            imei = text
            try:
                check_result = imei_check_request(imei, IMEI_API_TOKEN)
                bot.send_message(message.chat.id, check_result)
            except BaseException:
                bot.send_message(message.chat.id, f'ошибка по запросу: {text}')

    def handle(self, *args, **kwargs):
        bot.infinity_polling()
