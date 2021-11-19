from game.actor import Actor
from game.point import Point
from game import constants

class Paddles():
   """
   This class has everything to do with the two paddles used in the game.
   """
   def __init__(self):
      super().__init__()
      self._paddles= []
      self._constants = constants