#!/usr/bin/env python3
"""Guess the progression and fulfill the missing element."""

from brain_games import interface
from brain_games.games.progression_game import progression


def main():
    username = interface.welcome_user('progression_game')
    user_wins = progression()
    if user_wins:
        interface.say_congrats(username)
    else:
        interface.say_try_again(username)


if __name__ == '__main__':
    main()
