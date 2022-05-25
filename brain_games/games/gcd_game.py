from random import randint
import math
from brain_games import interface
from brain_games.consts import LOWER_BORDER, UPPER_BORDER, WINS_COUNT_REQUIRED


def gcd():
    round_count = 0
    user_winning = True

    while round_count < WINS_COUNT_REQUIRED and user_winning:
        round_count += 1
        num1 = randint(LOWER_BORDER, UPPER_BORDER)
        num2 = randint(LOWER_BORDER, UPPER_BORDER)
        interface.give_task(f'{num1} {num2}')

        user_answer = interface.get_answer()
        correct_answer = math.gcd(num1, num2)

        user_winning = (user_answer == str(correct_answer))

        if user_winning:
            interface.say_correct()
        else:
            interface.say_wrong_correct(user_answer, correct_answer)

    return user_winning
