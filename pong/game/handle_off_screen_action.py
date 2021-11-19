from game.action import Action
from game.point import Point
from game import constants
from game.actor import Actor
from game.move_actors_action import MoveActorsAction

class HandleOffScreenAction():
   """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
   Stereotype:
        Controller
   """
   def __init__(self):
      super().__init__()
      self.constants = constants
      self.move_actors_action = MoveActorsAction()

   def execute(self, cast):
      """Executes the action using the given actors.

      Args:
         cast (dict): The game actors {key: tag, value: list}.
      """