from emoji import emojize
from random import choice, randint
from telegram import KeyboardButton, ReplyKeyboardMarkup

import settings

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def play_random_numbers(user_number):
    bot_number = randint(user_number-10, user_number+10)
    if user_number > bot_number:
        message = (f"You're number is {user_number}",
        f", mine number is {bot_number} - You're winning!")
    elif user_number == bot_number:
        message = (f"You're number is {user_number}"
        f", mine number is {bot_number} - Draw!")
    elif user_number < bot_number:
        message = (f"You're number is {user_number}",
        f", mine number is {bot_number} - Bot is winning!")
    return message

def main_keyboard():
    return ReplyKeyboardMarkup([
        ['Give me a pussy', 
        KeyboardButton('My location', request_location=True)]
        ])
