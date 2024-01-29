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


def formatDexMessage(pools):
    print(pools)
    message = ""

    for pool in pools:
        label = "-"
        if pool.get('labels') is not None:
            label = pool['labels'][0]
        message += f"""
*_{pool['baseToken']['symbol']}/{pool['quoteToken']['symbol']}_*
{"Pool:":<27}{pool['chainId']}-{pool['dexId']}{label}
{"Current Price:":<20}{"$" + pretty_print_numbers(pool['priceUsd'])}
{"24 Change:":<20}{pool['priceChange']['h24']:.2f}%
{pool['url']}
"""
        print("@@@@@@@", message)

    return message
# {"Market Cap:":<20}{pretty_print_numbers(marketcap)}
# {"FDV:":<26}{pretty_print_numbers(fdv)}
# {"MC/FDV ratio:":<20}{pretty_print_numbers(market_cap_fdv_ratio*100)} %


def fuzzy_search_coin_id(input):
    url = f'https://api.dexscreener.com/latest/dex/search?q={input}'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if data.get('error') is not None:
        raise (f"{data['error']}")

    # return top 3 pools
    return data['pairs'][0:2]


def get_dex_data(coin_id):
    pools = fuzzy_search_coin_id(coin_id)

    return pools


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
