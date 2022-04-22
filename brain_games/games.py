"""The module to realize all games logic."""
from random import randint

from prompt import string

LOWER_BORDER = 1
UPPER_BORDER = 50
WINS_COUNT_REQUIRED = 3


def _get_wrong_correct_answer_string(user_ans, correct):
    """Return place user_ans and correct to the templated string."""
    return f"'{user_ans}' is wrong answer ;(. Correct answer was '{correct}'."


def even():
    """Even game. Returns True if user wins and False if fails."""
    wins_count = 0
    user_winning = True

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while wins_count < WINS_COUNT_REQUIRED and user_winning:
        game_number = randint(LOWER_BORDER, UPPER_BORDER)
        number_is_even = (game_number % 2 == 0)
        print('Question:', game_number)
        answer = string('Your answer: ')

        if number_is_even:
            if answer == 'yes':
                response = 'Correct!'
                user_winning = True
                wins_count += 1
            else:
                response = _get_wrong_correct_answer_string(answer, 'yes')
                user_winning = False

        else:
            if answer == 'no':
                response = 'Correct!'
                user_winning = True
                wins_count += 1
            else:
                response = _get_wrong_correct_answer_string(answer, 'no')
                user_winning = False
        print(response)

    return user_winning
