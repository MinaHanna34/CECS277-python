""" 
In this lab I created a rock-paper-scissors game. In this program I made the player play R-P-S with the computer. I did so by making a random Generator that picks from the three choices. I also made a menu where the user can check if he wants to start,check score or quit by picking 1,2 or 3.  
"""

import random 
import check_input


def weapon_menu():
  print("Choose your weapon: ")
  print("R. Rock")
  print("P. Paper")
  print("S. Scissors")
  print("B. Back")
  playerRPS = input()
  while playerRPS != "R" and playerRPS != "P" and playerRPS != "S" and playerRPS != "B":
    print('Invalid input')
    playerRPS=input()
  if playerRPS == "R":
    return "R"
  if playerRPS == "S":
    return "S"
  if playerRPS == "P":
    return "P"
  if playerRPS == "B":
    return "B"
  # here I were able to print the weapon menu and return the values the player choices to play
def comp_weapon():
  randomRPS = random.randrange(0, 3, 1)
  
  if randomRPS == 0:
    return "R"
  elif randomRPS == 1:
    return "P"
  elif randomRPS == 2:
    return "S"
  
#here is the random Generator  for the computer against the player
      
def find_winner(player, comp):
  if player == "R" and comp == "R" or player == "S" and comp == "S" or player == "P" and comp == "P":
    if player == "R":
      print("You chose Rock")
      print("Computer chose Rock")
      print("Tie")
      return 0
    if player == "P":
      print("You chose Paper")
      print("Computer chose Paper")
      print("Tie")
      return 0
    if player == "S":
      print("You chose Scissors")
      print("Computer chose Scissors")
      print("Tie")
      return 0

  if player == "R" and comp == "S":
    print("Player chose Rock")
    print("Computer chose Scissors")
    print("Player wins")
    return 1
  if player == "S" and comp == "R":
    print("Player chose Scissors")
    print("Computer chose Rock")
    print("Computer wins")
    return 2

  if player == "S" and comp == "P":
    print("Player chose Scissors")
    print("Computer chose Paper")
    print("Player wins")
    return 1
  if player == "P" and comp == "S":
    print("Player chose Paper")
    print("Computer chose Scissors")
    print("Computer wins")
    return 2

  if player == "P" and comp == "R":
    print("Player chose Paper")
    print("Computer chose Rock")
    print("Player wins")
    return 1
  if player == "R" and comp == "P":
    print("Player chose Rock")
    print("Computer chose Paper")
    print("Computer wins")
    return 2
      
# This is how to calculate if the computer won or the player. If the player won it would return 1 or if the computer won it would return 2.
def display_scores(player, comp):
  print("Player =", player)
  print("Computer =", comp)
  
#It calculate the total score of the player and the computer.
  
  
def main():
  player_choice = 0
  notDone = False
  playerscore = 0
  computerscore = 0
  
  while notDone == False:
    if player_choice == 3:
      print("Final Score:")
      display_scores(playerscore,computerscore)
      notDone = True
      return None

    userWeapon = ""

    if player_choice != "B":
      if player_choice == 1:
        while userWeapon != "B":
          userWeapon = weapon_menu()
          computerWeapon = comp_weapon()
          tracker = find_winner(userWeapon, computerWeapon)
          if tracker == 1:
            playerscore += 1
          if tracker == 2:
            computerscore += 1
      elif player_choice == 2:
        print("Scores")
        display_scores(playerscore,computerscore)
          
    print("RPS Menu:")
    print("1. Play game")
    print("2. Show score")
    print("3. Quit")
    player_choice = check_input.get_int_range("" , 1, 3)

#I mainly used main to be able to call on funcations and loop the menu.

        
        
      


main()

