from random import randint

from brain_games import interface

from brain_games.consts import LOWER_BORDER, UPPER_BORDER


def even_round():
    game_number = randint(LOWER_BORDER, UPPER_BORDER)
    interface.give_task(game_number)
    user_answer = interface.get_answer()

    if game_number % 2 == 0:
        correct_answer = 'yes'

    else:
        correct_answer = 'no'

    return user_answer, correct_answer
