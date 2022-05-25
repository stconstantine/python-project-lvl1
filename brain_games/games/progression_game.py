from random import randint
from brain_games import interface
from brain_games.consts import PROG_LEN_LOW_BORDER, PROG_LEN_UPPER_BORDER, \
    PROG_STEP_LOW, PROG_STEP_UPPER


def progression_round():

    prog_length = randint(PROG_LEN_LOW_BORDER, PROG_LEN_UPPER_BORDER)
    question_pos = randint(1, prog_length - 2)
    prog_step = randint(PROG_STEP_LOW, PROG_STEP_UPPER)
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

    return user_winning, user_answer, correct_answer
