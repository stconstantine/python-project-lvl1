"""
Module to perform a common logic for all games.

Function game() calls distinct game module,
which has to return tuple of 2 values:
    user_answer: str = last answer, received from user
    correct_answer: str = correct answer for this round
"""

from brain_games import interface

from brain_games.consts import WINS_COUNT_REQUIRED
from brain_games.games import calc_game, even_game, \
    gcd_game, prime_game, progression_game


def game(game_name):
    round_count = 0
    user_winning = True
    username = interface.welcome_user(game_name)

    game_names_catalog = {'calc_game': calc_game.calc_round,
                          'even_game': even_game.even_round,
                          'gcd_game': gcd_game.gcd_round,
                          'prime_game': prime_game.prime_round,
                          'progression_game': progression_game.progression_round
                          }

    get_round_results = game_names_catalog[game_name]

    while round_count < WINS_COUNT_REQUIRED and user_winning:
        round_count += 1
        user_answer, correct_answer = get_round_results()
        user_winning = (user_answer == correct_answer)
        if user_winning:
            interface.say_correct()
        else:
            interface.say_wrong_correct(user_answer, correct_answer)

    if user_winning:
        interface.say_congrats(username)
    else:
        interface.say_try_again(username)
