import Levels

import time
import random

# Print the instructions for the users
def print_instructions():
    print("RULES")
    print("-----------------------------------------------------------------------------")
    print("1) There are 10 multiple choice questions. You must select the right answer.")
    print("2) Every right answer gives you 10 points, otherwise no points ")
    print("3) You have two life lines. They are as follows:")
    print("			50:50 ........ Eliminate 2 wrong answers.")
    print("			Skip.......... You skip the qusetion.")
    print("			friend maybe).")
    print("If you don't use one help win 5 points more")
    print("If you don't use any help win 10 points more  ")
    print("4) Answer all the questions correctly")
    print("Good Luck :)")
    print("-----------------------------------------------------------------------------")


# Defines the available lifelines
def all_lifelines():
    list = ['50:50', 'Skip']
    return list


# Returns the question to be asked along with possible answers
def ask_question(turn):
    key = {1: Levels.level_1(), 2: Levels.level_2(), 3: Levels.level_3(), 4: Levels.level_4(), 5: Levels.level_5(), 6: Levels.level_6(), 7: Levels.level_7(), 8: Levels.level_8(),
           9: Levels.level_9(), 10: Levels.level_10()}

    Q, choices, ans = key[turn]

    # Prints the question
    print(Q)

    # Shows the multiple choices
    for key, value in choices.items():
        print(key, ':', value)
    print("\n")
    # return the correct answer
    return Q, choices, ans


# Returns the result of the lifeline that was used
def use_lifeline(Response, choices, ans):
    # Remove 2 wrong answers
    if Response == '50:50':
        ans_key = 0
        i = 0
        for key, value in choices.items():
            if choices[key] == ans:
                ans_key = key
                break
            else:
                i += 1

        indices = list(range(0, 4))
        indices.remove(i)
        remove = random.sample(indices, 2)
        letter_key = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

        for num in remove:
            choices[letter_key[num]] = ' '

        # Shows the multiple choices
        for key, value in choices.items():
            print(key, ':', value)

        return choices

    # skip the question
    else:
        print('You use the "Skip" Help!! Here is the new question!!')
        key = {11: Levels.level_11()}
        Q, choices, ans = key[11]

        print(Q)
        for key, value in choices.items():
            print(key, ':', value)
        print("\n")

        return choices


def exit_game():
    quit()