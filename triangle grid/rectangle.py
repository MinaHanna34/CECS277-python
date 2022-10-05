""" 
In Rectangle I just set the attributes to be able to use them.

"""


class Rectangle:
    x = 0
    y = 0
    width = 0
    height = 0
    """ 
  I then used init to use the class. I then set self to width and height.

  """

    def __init__(self, w, h, x=0, y=0):
        self.width = w
        self.height = h

    """ 
  For get coords I return the self x and self y.
  """

    def get_coords(self):
        return f"({self.x}, {self.y})"

    """ 
  In get_width I return self width
  """

    def get_width(self):
        return self.width

    """
  In get_height I return self height
  """

    def get_height(self):
        return self.height

    """
  For move up I subtracted 1 from self x to be able to go up, then I return self.
  """

    def move_up(self):
        self.x = self.x - 1
        return self

    """
  In move down for selfx I added one, then return self.
  """

    def move_down(self):
        self.x = self.x + 1
        return self

    """
  In move right I added 1 to selfy then return self.
  """

    def move_right(self):
        self.y = self.y + 1
        return self

    """
  In move left I subracted 1 to selfy then return self.
  """

    def move_left(self):
        self.y = self.y - 1
        return self
