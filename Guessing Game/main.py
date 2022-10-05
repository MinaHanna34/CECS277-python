"""
In this program, I created a "Guessing Game." The program generates a random number then prompts the user to guess a number. The program will let the user know if the number is invalid, too high, or too low compared to the random number. When the user guesses the correct number, the program displays a congratulatory message along with the number of tries that it took.
"""

def main():

  import check_input
  import random


  guessedCorrect = False
  #  Boolean to set a condition for our while loop
  
  count = 1
  #  Variable that stores each time the user guesses a number
  
  randomNumber = random.randrange(1, 100, 1)
  #  Variable that stores (and does not change) a random number



  print("- Guessing Game -")

  print("I'm thinking of a number.", end='')
  guessedNum = check_input.get_int_range(" Make a guess (1-100): ", 1, 100)
  #  Variable that prompts the user for a number and stores it
  



  while guessedCorrect == False:
  #  Loop that executes until the user guesses the random number. Takes in the user guesses and   returns whether or not the guess is invalid, too low, or too high.

    if guessedNum > randomNumber:
      print("Too high! ", end='')
      guessedNum = check_input.get_int_range("Guess again (1-100): ", 1, 100)
      count += 1
    elif guessedNum < randomNumber:
      print("Too low! ", end='')
      guessedNum = check_input.get_int_range("Guess again (1-100): ", 1, 100)
      count += 1
    elif guessedNum == randomNumber:
      print(f"Correct! You got it in {count} tries.")
      guessedCorrect = True

main()
  
  