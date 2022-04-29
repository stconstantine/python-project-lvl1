#!/usr/bin/env python3
"""Is even? game."""

from brain_games.games.even_game import even
from brain_games import interface


def main():

    username = interface.welcome_user('even_game')
    user_wins = even()
    if user_wins:
        interface.say_congrats(username)
    else:
        interface.say_try_again(username)


if __name__ == '__main__':
    main()
