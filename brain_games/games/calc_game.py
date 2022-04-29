from random import randint, choice

from brain_games import interface

LOWER_BORDER = 0
UPPER_BORDER = 50
WINS_COUNT_REQUIRED = 3
OPERANDS = ['+', '-', '*']


def calc():
    round_count = 0
    user_winning = True

    while round_count < WINS_COUNT_REQUIRED and user_winning:
        round_count += 1
        expr = f'{randint(LOWER_BORDER, UPPER_BORDER)}' \
               f' {choice(OPERANDS)} ' \
               f'{randint(LOWER_BORDER, UPPER_BORDER)}'
        interface.give_task(expr)

        user_answer = interface.get_answer()
        user_winning = (user_answer == str(eval(expr)))

        if user_winning:
            interface.say_correct()
        else:
            interface.say_wrong_correct(user_answer, eval(expr))

    return user_winning
