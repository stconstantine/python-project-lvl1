from random import randint
from brain_games import interface
from brain_games.consts import LOWER_BORDER, UPPER_BORDER, \
    WINS_COUNT_REQUIRED, PRIMES


def prime():
    round_count = 0
    user_winning = True

    while round_count < WINS_COUNT_REQUIRED and user_winning:
        round_count += 1
        game_number = randint(LOWER_BORDER, UPPER_BORDER)
        number_is_prime = game_number in PRIMES

        interface.give_task(game_number)
        answer = interface.get_answer()

        if number_is_prime:
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
