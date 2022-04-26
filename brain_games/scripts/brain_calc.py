#!/usr/bin/env python3
"""Solve the expression"""
from brain_games import interface
from brain_games.games.calc_game import calc


def main():
    username = interface.welcome_user()
    user_wins = calc()
    if user_wins:
        interface.say_congrats(username)
    else:
        interface.say_try_again(username)


if __name__ == '__main__':
    main()
