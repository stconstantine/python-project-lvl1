import prompt


def welcome_user(game: str):
    """Prompts user to input the username then print greeting."""
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your username? ')
    print(f'Hello, {username}!')
    rules_catalog = {'calc_game': 'What is the result of the expression?',
                     'even_game': 'Answer "yes" if the number is even, otherwise answer "no".',
                     'gcd_game': 'Find the greatest common divisor of given numbers.',
                     'prime_game': 'Answer "yes" if given number is prime. Otherwise answer "no".',
                     'progression_game': 'What number is missing in the progression?'
                     }

    print(rules_catalog[game])

    return username


def give_task(task):
    print('Question:', task)


def get_answer():
    return prompt.string('Your answer: ')


def say_correct():
    print('Correct!')


def say_congrats(username):
    print(f'Congratulations, {username}!')


def say_try_again(username):
    print(f'Let\'s try again, {username}!')


def say_wrong_correct(wrong, correct):
    print(f"'{wrong}' is wrong answer ;(. Correct answer was '{correct}'.")
