from random import randint
from brain_games import interface
from brain_games.consts import LOWER_BORDER, UPPER_BORDER, PRIMES


def prime_round():
    game_number = randint(LOWER_BORDER, UPPER_BORDER)
    interface.give_task(game_number)
    user_answer = interface.get_answer()

    if game_number in PRIMES:
        correct_answer = 'yes'

    else:
        correct_answer = 'no'

    user_winning = (user_answer == correct_answer)

    return user_winning, user_answer, correct_answer
