from config import bot
from pendle import formatMessage, get_data, last_check
from scheduler import start_schedule
from utils import pretty_print_telebot_message


# Handle /pendle command
@bot.message_handler(commands=['pendle'])
def pendle_price_check(message):
    data_YTeeth, data_YTrseth = get_data()

    reply = formatMessage(data_YTeeth, data_YTrseth)
    last_check["yt_eeth_apy"] = data_YTeeth
    last_check["yt_rseth_apy"] = data_YTrseth

    bot.send_message(
        message.chat.id,
        reply,
        parse_mode='MarkdownV2')


# Handle /p command
@bot.message_handler(commands=['p'])
def coin_price_check(message):
    data_YTeeth, data_YTrseth = get_data()

    reply = formatMessage(data_YTeeth, data_YTrseth)
    last_check["yt_eeth_apy"] = data_YTeeth
    last_check["yt_rseth_apy"] = data_YTrseth

    bot.send_message(
        message.chat.id,
        reply,
        parse_mode='MarkdownV2')


# Handle all uncaught messages
@bot.message_handler(func=lambda m: True)
def handle_all_messages(message):
    pretty_print_telebot_message(message)
    print(
        f"[ChatID: {message.chat.id}]Received message from user {message.from_user.username} ({message.from_user.id}): {message.text}")


# Run scheduler
start_schedule()

bot.polling()
