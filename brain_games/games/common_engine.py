from brain_games.consts import WINS_COUNT_REQUIRED
from brain_games.games import calc_game
from brain_games import interface
"""
Function game() calls distinct game module,
which has to return tuple of 3 values:
    user_winning = TRUE if user won this round of FALSE if not
    user_answer: str = last answer, received from user
    correct_answer: str = correct answer for this round
"""


def game(game_name):
    round_count = 0
    user_winning = True

    username = interface.welcome_user(game_name)

    if game_name == 'calc_game':
        get_round_results = calc_game.calc_round
    else:
        print(f'ERROR! Was called the game {game_name} '
              f'in common_engine. No such a game!')
        return

    while round_count < WINS_COUNT_REQUIRED and user_winning:
        round_count += 1
        user_winning, user_answer, correct_answer = get_round_results()
        if user_winning:
            interface.say_correct()
        else:
            interface.say_wrong_correct(user_answer, correct_answer)

    if user_winning:
        interface.say_congrats(username)
    else:
        interface.say_try_again(username)
