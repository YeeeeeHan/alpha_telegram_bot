import requests

from config import bot, getChatIdFromEnv
from utils import formatInputForMarkdown, pretty_print_numbers

last_check = {
    "current_price": 0,
    "market_cap": 0,
    "fdv": 0,
    "market_cap_fdv_ratio": 0,
}


def render_up_or_down(value):
    if value > 0:
        return "📈"
    elif value < 0:
        return "📉"
    else:
        return "🔷"


def calculatePercentageChange(new, old):
    difference = (new - old)/old
    retVal = round(difference * 100, 3)
    return (retVal, render_up_or_down(retVal))


def formatCoinMessage(coin_id, marketcap, fdv, market_cap_fdv_ratio, currentprice):
    return f"""
*_{coin_id}_*
{"Current Price:":<20}{"$" + pretty_print_numbers(currentprice)}
{"Market Cap:":<20}{pretty_print_numbers(marketcap)}
{"FDV:":<26}{pretty_print_numbers(fdv)}
{"MC/FDV ratio:":<20}{pretty_print_numbers(market_cap_fdv_ratio*100)} %
"""


def get_coin_data(coin_id):
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}'
    response = requests.get(url)
    response.raise_for_status()
    coin_data = response.json()

    if coin_data.get('error') is not None:
        raise (f"{coin_data['error']}")

    marketcap = coin_data['market_data']["market_cap"]["usd"]
    fdv = coin_data['market_data']["fully_diluted_valuation"]["usd"]
    market_cap_fdv_ratio = coin_data['market_data']["market_cap_fdv_ratio"]
    current_price = coin_data['market_data']["current_price"]["usd"]

    return marketcap, fdv, market_cap_fdv_ratio, current_price


# def price_alert():
#     data_YTeeth, data_YTrseth = get_coin_data()

#     message = formatMessage(data_YTeeth, data_YTrseth)

#     if data_YTeeth < 28.5 or data_YTrseth < 28.5:
#         bot.send_message(
#             getChatIdFromEnv(),
#             message,
#             parse_mode='MarkdownV2')

#         bot.send_message(
#             getChatIdFromEnv(),
#             formatInputForMarkdown(
#                 "YT eETH IS LESS THAN 0.285% APY. WE GOT FUCKED BY HEEHAWN. SELL SELL SELL."),
#             parse_mode='MarkdownV2')

#         bot.send_message(
#             getChatIdFromEnv(),
#             formatInputForMarkdown(
#                 "YT rsETH IS LESS THAN 0.285% APY. WE GOT FUCKED BY HEEHAWN. SELL SELL SELL."),
#             parse_mode='MarkdownV2')
