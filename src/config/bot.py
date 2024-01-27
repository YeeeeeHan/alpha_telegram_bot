import logging
import os

import telebot

from utils import TELEGRAM_BOT_TOKEN

# Get the bot token from .env file
BOT_TOKEN = os.getenv(TELEGRAM_BOT_TOKEN)
bot = telebot.TeleBot(BOT_TOKEN)

# Enable TeleBot logging
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
