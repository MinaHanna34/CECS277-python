import random
"""
Die is used for the number of sides in the dice and the value of the rolled dice.
"""
class Die:
  """
  init will sort the three dices and makes the player points 0
  """
  def __init__(self, sides=6):
    self.sides = sides
  """
  In roll, it makes a random number starting from 1. Then it returns randomroll
  """
  def roll(self):
    randomRoll = random.randint(1, self.sides)
    return randomRoll
  """
  __str__ will return die as a string
  """
  def __str__(self, other) :
    return f'str({self.die})'
  """
  __it__ will return if the value of self is less then other
  """
  def __lt__(self, other):
    if self < other:
      return True
    else:
      return False
  """
  __eq__ will return if self is equal to other.
  """
  def __eq__(self, other):
    if self == other:
      return True
    else:
      return False
  """
  _sub_ subtracits self and other then returns it.
  """
  def __sub__(self, other):
    return (self-other)