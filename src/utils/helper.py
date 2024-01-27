from pprint import pprint

import telebot


def parseCommandSource(message: telebot.types.Message) -> int:
    return message.chat.id


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
