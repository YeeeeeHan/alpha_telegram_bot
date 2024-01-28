from pprint import pprint

import telebot


def parseCommandSource(message: telebot.types.Message) -> int:
    return message.chat.id


# Find and replace all '.' with '\.'
def formatInputForMarkdown(input):
    return str(input).replace('.', '\.').replace('-', '\-')


def pretty_print_numbers(input):
    number = float(input)
    if number < 0.0001:
        return f"{number:.8f}"
    elif number < 1:
        return f"{number:.5f}"
    elif number < 100:
        return f"{number:.2f}"
    elif number < 1_000_000:
        return f"{number:,}"
    elif number < 1_000_000_000:
        return f"{number / 1_000_000:,.3f} M"
    else:
        return f"{number / 1_000_000_000:,.3f} B"


# Pretty print a telebot message
def pretty_print_telebot_message(message: telebot.types.Message):
    message_data = {
        'message_id': message.message_id,
        'text': message.text,
        'from_user': {
            'id': message.from_user.id,
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
            'username': message.from_user.username,
        },
        'date': message.date,
        'chat': {
            'id': message.chat.id,
            'type': message.chat.type,
            'title': message.chat.title,
            'username': message.chat.username,
        },
    }

    pprint(message_data)
