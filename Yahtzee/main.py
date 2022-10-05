"""
In this lab, I created the game called Yahtzee. In this program,  learned more about how to use classes and call on them from different files. I then created 3 files main, player,die. Die was mainly used to generate a dice role. Player was used for points and if the user got a pair or better. Then I used main to call the functions and loop them.
"""

import die
import player
import random
import check_input
"""
In take turn, I passed the player object and used rolledlist to get the random dice. I also then used the score to see if the player got a three-of-a-kind, a pair , or none.

"""
def take_turn(object):
  rolledList = []
  rolledList = object.roll_dice()
  print(f'D1={rolledList[0]} D2={rolledList[1]} D3={rolledList[2]}')
  if(object.has_three_of_a_kind() == True):
    print("You got a 3 of a kind!")
    
  elif(object.has_pair() == True):
    print('You got a pair!')
  elif (object.has_series() == True):
    print("You got a series of 3!")
  else:
    print("Awww. Too bad")
  return 
"""
For main I used it to print the functions and loop the menu. I then kept track of the score and if the player still wanted to play the game or not. If the player chooses not to the game ends.
"""
def main():
  print('-Yahtzee- ')
  p1 = player.Player()
  
  condition = False

  while condition != True:
    take_turn(p1)
    print("Score =", p1.get_points())
    user = check_input.get_yes_no("Want to continue? (Y/N)")
    if user == False:
      condition = True
    elif user == True:
      condition = False
  print("Game over.")
  print("Final score =", p1.get_points())
  

  return

main()