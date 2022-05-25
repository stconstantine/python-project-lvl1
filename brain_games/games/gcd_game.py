"""
Module to perform a one round in gcd game.
Function gcd_round randomly generates two numbers and
asks a user to determine the greatest common divisor of them.
Returns a user answer and a correct answer.
"""

import math
from random import randint

from brain_games import interface

from brain_games.consts import LOWER_BORDER, UPPER_BORDER


def gcd_round():

    num1 = randint(LOWER_BORDER, UPPER_BORDER)
    num2 = randint(LOWER_BORDER, UPPER_BORDER)

    interface.give_task(f'{num1} {num2}')
    user_answer = interface.get_answer()

    correct_answer = str(math.gcd(num1, num2))

    return user_answer, correct_answer
