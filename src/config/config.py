import logging
import os

import telebot
from dotenv import load_dotenv

from utils import (DEV_CHAT_ID, ENV, PROD_CHAT_ID, TELEGRAM_BOT_TOKEN,
                   TELEGRAM_BOT_TOKEN_DEV)

load_dotenv()


def getChatIdFromEnv():
    # Get the bot token from .env file, according to the ENV variable
    if os.getenv(ENV) == "dev":
        return DEV_CHAT_ID
    else:
        BOT_TOKEN = os.getenv(TELEGRAM_BOT_TOKEN)
        bot = telebot.TeleBot(BOT_TOKEN)
        return PROD_CHAT_ID


def getBotFromEnv():
    # Get the bot token from .env file, according to the ENV variable
    if os.getenv(ENV) == "dev":
        DEV_BOT_TOKEN = os.getenv(TELEGRAM_BOT_TOKEN_DEV)
        bot = telebot.TeleBot(DEV_BOT_TOKEN)
        return bot
    else:
        BOT_TOKEN = os.getenv(TELEGRAM_BOT_TOKEN)
        bot = telebot.TeleBot(BOT_TOKEN)
        return bot


bot = getBotFromEnv()

# Enable TeleBot logging
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
