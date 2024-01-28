import requests

from coins import formatCoinMessage, get_coin_data
from config import bot
from pendle import formatPendleMessage, get_pendle_data, last_check
from scheduler import start_schedule
from utils import formatInputForMarkdown


# Handle /pendle command
@bot.message_handler(commands=['pendle'])
def pendle_price_check(message):
    data_YTeeth, data_YTrseth = get_pendle_data()

    reply = formatPendleMessage(data_YTeeth, data_YTrseth)
    last_check["yt_eeth_apy"] = data_YTeeth
    last_check["yt_rseth_apy"] = data_YTrseth

    bot.send_message(
        message.chat.id,
        reply,
        parse_mode='MarkdownV2')


# Handle /p command
@bot.message_handler(commands=['p'])
def coin_price_check(message):
    command_parts = message.text.split(maxsplit=1)
    if len(command_parts) != 2:
        return

    coin_id = command_parts[1]
    try:
        id, name, symbol, marketcap, fdv, market_cap_fdv_ratio, currentprice = get_coin_data(
            coin_id)
        bot.send_message(
            message.chat.id,
            formatInputForMarkdown(formatCoinMessage(
                id, name, symbol, marketcap, fdv, market_cap_fdv_ratio, currentprice)),
            parse_mode='MarkdownV2')

    except Exception as e:
        bot.send_message(
            message.chat.id,
            formatInputForMarkdown(f"{e}"),
            parse_mode='MarkdownV2')
        return

# Handle all uncaught messages


@bot.message_handler(func=lambda m: True)
def handle_all_messages(message):
    print(
        f"[ChatID: {message.chat.id}]Received message from user {message.from_user.username} ({message.from_user.id}): {message.text}")


# Run scheduler
start_schedule()

bot.polling()
