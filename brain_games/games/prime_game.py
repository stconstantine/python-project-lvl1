"""
Module to perform a one round in prime game.
Function prime_round randomly generates a number and
asks a user if it is prime or not. User must type 'yes' or 'no'
Uses a list of primes from brain_games.consts.PRIMES
Returns a user answer and a correct answer.
"""

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

    return user_answer, correct_answer
