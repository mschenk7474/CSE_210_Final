from game.actor import Actor
from game.point import Point
from game import constants
import random

class Ball():
   """
   This class will have everything that has to do with the ball.
   """
   def __init__(self):
      super().__init__()
      self._ball = []
      self._constants = constants
      


   def set_ball(self):
      ints = [18, -18]
      self._random_x_velo = random.choice(ints)
      self._random_y_velo = random.randint(-5, 5)
      if self._random_y_velo == 0:
         self._random_y_velo = random.randint(-1, 1)

      ball = Actor()
      ball_position = Point(400, 300)
      #No image yet
      ball_image = self._constants.IMAGE_BALL
      ball_width = self._constants.BALL_WIDTH
      ball_height = self._constants.BALL_HEIGHT
      ball_velocity = Point(self._random_x_velo, self._random_y_velo)
      ball.set_position(ball_position)
      ball.set_image(ball_image)
      ball.set_width(ball_width)
      ball.set_height(ball_height)
      ball.set_velocity(ball_velocity)
      
      self._ball.append(ball)

   def get_ball(self):
      """
      Returns the list to be used elsewhere.
      """
      return self._ball