import die
"""
  Player will have a list of 3-day objects and will have the player's points.
"""
class Player:

  """
  __init__ was used to sort the list of all the die1,die2,di3 and se tthe player points to 0
  """
  def __init__(self, playerPoints=0, dieList=[]):
    self.playerPoints = playerPoints
    self.die1 = die.Die(6)
    self.die2 = die.Die(6)
    self.die3 = die.Die(6)
    self.dieList = []
  """
  In get_points I returned how many points the player got.
  """
  def get_points(self):
    return self.playerPoints
  
  """
  For roll_dice it will call the roll and will sort dielist then return it.
  """
    
  def roll_dice(self):
    self.dieList.clear()
    rolled1 = self.die1.roll()
    rolled2 = self.die2.roll()
    rolled3 = self.die3.roll()
    self.dieList.append(rolled1)
    self.dieList.append(rolled2)
    self.dieList.append(rolled3)
    self.dieList.sort()
    return self.dieList
    
  """
  has_pair will return true if two dices are the same then add 1 point.
  """
  def has_pair(self):

    if self.dieList[0] == self.dieList[1] or self.dieList[1] == self.dieList[2] or  self.dieList[0] == self.dieList[2]:
      self.playerPoints += 1
      return True
    else:
      return False

  """
  has_three_of_a_kind will return if 3 of the dice are the same and add 3 points to the player.
  """
  def has_three_of_a_kind(self):
    if self.dieList[0] == self.dieList[1] and self.dieList[0] == self.dieList[2]:
      self.playerPoints += 3
      return True
    else:
      return False
  """
  has_series will return true if the dice are in a sequence and will add 2 points to the player.
  """
  def has_series(self):
    if (self.dieList[0] == 1 and self.dieList[1] == 2 and self.dieList[2] == 3) or (self.dieList[0] == 2 and self.dieList[1] == 3 and self.dieList[2] == 4) or (self.dieList[0] == 3 and self.dieList[1] == 4 and self.dieList[2] == 5) or (self.dieList[0] == 4 and self.dieList[1] == 5 and self.dieList[2] == 6):
      self.playerPoints += 2
      return True
    else:
      return False
  """
  __str__ will return a string and print the dice rolls.
  """
  def __str__(self):
    return f'D1 = {self.die1}, D2 = {self.die2}, D3 = {self.die3}'