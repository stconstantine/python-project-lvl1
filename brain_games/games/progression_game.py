"""
Module to perform a one round in progression game.
Function progression_round generates an arithmetic progression
with a random step and removes random member, asking user to guess it.
Uses some consts to variate the length of a progression,
and a range of possible step values. User must type a number.
Returns a user answer and a correct answer.
"""

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

    return user_answer, correct_answer
