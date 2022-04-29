#!/usr/bin/env python3
"""Is the number is prime?"""
from brain_games import interface
from brain_games.games.prime_game import prime


def main():
    username = interface.welcome_user('prime_game')
    user_wins = prime()
    if user_wins:
        interface.say_congrats(username)
    else:
        interface.say_try_again(username)


if __name__ == '__main__':
    main()
