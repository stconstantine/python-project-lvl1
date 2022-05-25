"""The module to realize even game logic."""
from random import randint
from brain_games import interface

LOWER_BORDER = 1
UPPER_BORDER = 50
WINS_COUNT_REQUIRED = 3


def even():
    """Even game. Returns True if user wins and False if fails."""
    round_count = 0
    user_winning = True

    while round_count < WINS_COUNT_REQUIRED and user_winning:
        round_count += 1

        game_number = randint(LOWER_BORDER, UPPER_BORDER)
        number_is_even = (game_number % 2 == 0)
        interface.give_task(game_number)
        answer = interface.get_answer()

        if number_is_even:
            if answer == 'yes':
                interface.say_correct()
                user_winning = True
            else:
                interface.say_wrong_correct(answer, 'yes')
                user_winning = False

        else:
            if answer == 'no':
                interface.say_correct()
                user_winning = True
            else:
                interface.say_wrong_correct(answer, 'no')
                user_winning = False

    return user_winning
