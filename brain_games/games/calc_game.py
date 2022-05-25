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
    user_winning = (user_answer == correct_answer)

    return user_winning, user_answer, correct_answer
