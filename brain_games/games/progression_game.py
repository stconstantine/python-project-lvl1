from random import randint
from brain_games import interface


WINS_COUNT_REQUIRED = 3


def progression():
    round_count = 0
    user_winning = True
    while round_count < WINS_COUNT_REQUIRED and user_winning:
        round_count += 1

        prog_length = randint(5, 12)
        question_pos = randint(1, prog_length - 2)
        prog_step = randint(1, 10)
        first_element = randint(0, prog_step)
        raw_progression = []
        for element in range(first_element,
                             prog_length * prog_step + first_element,
                             prog_step):
            raw_progression.append(str(element))

        masked_progression = list(raw_progression)
        masked_progression[question_pos] = ".."

        interface.give_task(' '.join(masked_progression))
        user_answer = interface.get_answer()
        correct_answer = raw_progression[question_pos]

        user_winning = (user_answer == correct_answer)

        if user_winning:
            interface.say_correct()
        else:
            interface.say_wrong_correct(user_answer, correct_answer)

    return user_winning
