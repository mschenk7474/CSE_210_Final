from game.action import Action
from game.point import Point
from game import constants

class MoveActorsAction():

   def execute(self,cast):
      """Executes the action using the given actors.

      Args:
         cast (dict): The game actors {key: tag, value: list}.
      """
      for group in cast.values():
         for actor in group:
            if not actor.get_velocity().is_zero():
               self._move_actor(actor)

   def _move_actor(self, actor):
      """Moves the given actor to its next position according to its 
      velocity. Will wrap the position from one side of the screen to the 
      other when it reaches the edge in either direction.
        
      Args:
         actor (Actor): The actor to move.
      """
      position = actor.get_position()
      velocity = actor.get_velocity()

      x = position.get_x()
      y = position.get_y()
      dx = velocity.get_x()
      dy = velocity.get_y()

      x = (x + dx) #% constants.MAX_X
      y = (y + dy) #% constants.MAX_Y
      
      position = Point(x, y)
      actor.set_position(position)