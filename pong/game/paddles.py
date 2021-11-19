from game.actor import Actor
from game.point import Point
from game import constants

class Paddles():
   """
   This class has everything to do with the two paddles used in the game.
   """
   def __init__(self):
      super().__init__()
      self._paddle_left= []
      self._paddle_right= []
      self._constants = constants

   def set_paddle_left(self):
      """
      Sets the left paddle up as an actor and gives it all of its properties.
      """
      paddleL = Actor()
      paddleL_position = Point(100, 300)
      #paddleL_image = self._constants.IMAGE_PADDLE
      paddleL_width = self._constants.PADDLE_WIDTH
      paddleL_height = self._constants.PADDLE_HEIGHT
     #paddleL.set_image(paddleL_image)
      paddleL.set_position(paddleL_position)
      paddleL.set_width(paddleL_width)
      paddleL.set_height(paddleL_height)

      self._paddle_left.append(paddleL)
   
   def get_paddle_left(self):
      """
      Returns the left paddle to be used elsewhere.
      """
      return self._paddle_left

   def set_paddle_right(self):
      """
      Sets the right paddle up as an actor and gives it all of its properties.
      """
      paddleR = Actor()
      paddleR_position = Point(650, 300)
      #paddleR_image = self._constants.IMAGE_PADDLE
      paddleR_width = self._constants.PADDLE_WIDTH
      paddleR_height = self._constants.PADDLE_HEIGHT
      paddleR.set_position(paddleR_position)
      #paddleR.set_image(paddleR_image)
      paddleR.set_width(paddleR_width)
      paddleR.set_height(paddleR_height)

      self._paddle_right.append(paddleR)
   
   def get_paddle_right(self):
      """
      Returns the right paddle to be used elsewhere.
      """
      return self._paddle_right