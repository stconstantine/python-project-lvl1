import prompt


def welcome_user():
    """Prompts user to input the username then print greeting."""
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your username? ')
    print(f'Hello, {username}!')
    return username


def give_task(task: str):
    print('Question:', task)


def get_answer(answer_type: str = ''):
    prompt_string = 'Your answer: '
    if answer_type == 'integer':
        return prompt.integer(prompt_string)
    else:
        return prompt.string(prompt_string)


def say_correct():
    print('Correct!')


def say_congrats(username):
    print(f'Congratulations, {username}!')


def say_try_again(username):
    print(f'Let\'s try again, {username}!')


def say_wrong_correct(wrong, correct):
    print(f"'{wrong}' is wrong answer ;(. Correct answer was '{correct}'.")
