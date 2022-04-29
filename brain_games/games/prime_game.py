from random import randint
from brain_games import interface
LOWER_BORDER = 1
UPPER_BORDER = 50
WINS_COUNT_REQUIRED = 3
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
          61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
          131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
          193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
          263, 269, 271]


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
