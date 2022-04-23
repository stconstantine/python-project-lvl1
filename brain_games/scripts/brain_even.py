#!/usr/bin/env python3
"""Is even? game."""

import brain_games.games as games
import prompt


def main():
    """Start game with greetings and farewells."""

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    user_won = games.even()
    if user_won:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')


if __name__ == '__main__':
    main()
