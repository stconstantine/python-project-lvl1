"""Module with command line functions."""
import prompt


def welcome_user():
    """Prompts user to input the name then print greeting."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
