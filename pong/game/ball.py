from game.actor import Actor
from game.point import Point
from game import constants

class Ball():
   """
   This class will have everything that has to do with the ball.
   """
   def __init__(self):
      super().__init__()
      self._ball = []
      self._constants = constants