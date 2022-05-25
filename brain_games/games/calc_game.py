"""
Module to perform a one round in calc game.
Function calc_round forms a math expression of two args with
binary OPERANDS and tasks a user to solve it.
Then calculates a correct result and
returns a user answer and a correct answer.
"""

from random import randint, choice

from brain_games import interface

from brain_games.consts import LOWER_BORDER, UPPER_BORDER, OPERANDS


def calc_round():
    expr = f'{randint(LOWER_BORDER, UPPER_BORDER)}' \
           f' {choice(OPERANDS)} ' \
           f'{randint(LOWER_BORDER, UPPER_BORDER)}'
    interface.give_task(expr)

    user_answer = interface.get_answer()
    correct_answer = str(eval(expr))

    return user_answer, correct_answer
