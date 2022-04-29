#!/usr/bin/env python3
"""Solve the expression"""
from brain_games import interface
from brain_games.games.gcd_game import gcd


def main():
    username = interface.welcome_user('gcd_game')
    user_wins = gcd()
    if user_wins:
        interface.say_congrats(username)
    else:
        interface.say_try_again(username)


if __name__ == '__main__':
    main()
