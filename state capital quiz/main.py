"""
In this lab, I created a state capital quiz. I did this by using the statecaptatils.txt and importing it. I then randomized it and made it so that it would print out something different every time. The user must guess the correct answers and get as much correct as possible.

"""

import random
import check_input
"""
In read_file_to_dict(file_name) I opened the file. I then split the list to be able to break the capital.I then stored them as a key value and return dict.
"""


def read_file_to_dict(file_name):
    file = open(file_name)
    dict = {}
    for state in file:
        splitList = state.strip().split(',')
        dict[splitList[0]] = splitList[1]
    return dict


"""
For get_random_state(states) It generates a random number and then converts the dictionary into a list of key values. Then it gives a randomstate and returns it.
"""


def get_random_state(states):

    randomNum = random.randint(0, 49)
    dictList = list(states.items())
    randomState = dictList[randomNum]
    return randomState


"""
In get_random_choices(states, correct_capital) I convert the dictlist into a list of values. Then I made the wronglist.I then got 3 wrong answers from random then added it to the wronglist. I then return wronglist.
"""


def get_random_choices(states, correct_capital):
    dictList = list(states.items())
    wrongList = []
    count = 0

    while count < 3:
        randomNum = random.randint(0, 49)

        if (dictList[randomNum]) not in (
                wrongList) and (dictList[randomNum]) != (correct_capital):
            wrongList.append(dictList[randomNum])
            count += 1
        elif (dictList[randomNum]) == (correct_capital):
            count = count

    wrongList.append(correct_capital)
    random.shuffle(wrongList)

    return (wrongList)


"""
In ask_question(correct_state, possible_answers) I made it print out the userinput. I then made sure the user only inputs A,B,C,D. If the user returns the correct letter. It return 0,1,2,3.
"""


def ask_question(correct_state, possible_answers):

    bool = False

    while bool == False:
        print('')
        userInput = input('Enter selection: ')

        if userInput == 'A' or userInput == 'B' or userInput == 'C' or userInput == 'D':
            if userInput == 'A':
                return 0
            elif userInput == 'B':
                return 1
            elif userInput == 'C':
                return 2
            elif userInput == 'D':
                return 3
            bool = True
        else:
            print("Invalid input. Input choice A-D.")

    return


"""
For the main function, I read the text file and added the score for the user if he gets the answer right. We then made a loop to display the other functions and give the choices A,B,C,D, and the wrong answers. If he guesses the right answer he gets a point until 10 times then it ends.
"""


def main():
    Spair = {}
    Spair.update(read_file_to_dict("StateCapitals.txt"))
    quizquest = 1
    correctguess = 0
    print('- State Capitals Quiz -')
    while quizquest < 11:
        correctAns = get_random_state(Spair)
        choices = get_random_choices(Spair, correctAns)
        print(f'{quizquest}. The capital of {correctAns[0]} is:')
        print(f'A. {choices[0][1]}', end=' ')
        print(f'B. {choices[1][1]}', end=' ')
        print(f'C. {choices[2][1]}', end=' ')
        print(f'D. {choices[3][1]}', end=' ')
        guesscheck = ask_question(correctAns, choices)
        quizquest += 1
        if choices[guesscheck][1] == correctAns[1]:
            print("Correct")
            correctguess += 1
        else:
            print("Incorrect! The correct answer is:", correctAns[1])
    print("End of test. You got", correctguess, "correct.")


main()
