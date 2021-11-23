from game.actor import Actor
from game.point import Point
from game.action import Action
from game import constants
from game.audio_service import AudioService
import random

class HandleCollisionsAction():
   def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = AudioService()

   def execute(self, cast):
      """Executes the action using the given actors. In this
      case, that means determining if the ball hits the paddle.

      Args:
         cast (dict): The game actors {key: tag, value: list}.
      """
      ball = cast["ball"][0]
      paddleL = cast["paddleL"][0]
      paddleR = cast["paddleR"][0]
      ball_velocity_x = ball._velocity._x
      ball_velocity_y = ball._velocity._y
      ball_velocity = ball.get_velocity()

      self._random_y_velo = random.randint(-1, 1)
      if self._random_y_velo == 0:
         self._random_y_velo = random.randint(-1, 1)

      if self._physics_service.is_collision(ball, paddleL):
         ball_velocity_x = ball_velocity_x * -1
         ball_velocity_y = self._random_y_velo
         ball_velocity = Point(ball_velocity_x, ball_velocity_y)
         ball.set_velocity(ball_velocity)
      elif self._physics_service.is_collision(ball, paddleR):
         ball_velocity_x = ball_velocity_x * -1
         ball_velocity_y = self._random_y_velo
         ball_velocity = Point(ball_velocity_x, ball_velocity_y)
         ball.set_velocity(ball_velocity)
      # balls = cast["balls"][0]
      # paddle = cast["paddle"][0]
      # bricks = cast["bricks"]
      # balls_velocity = balls.get_velocity()
      # if self._physics_service.is_collision(balls, paddle):
      #    self._audio_service.play_sound(constants.SOUND_BOUNCE)
      #    balls_velocity = Point(-10, -1)
      #    balls.set_velocity(balls_velocity)
      # for brick in bricks:
      #    if self._physics_service.is_collision(balls, brick):
      #       balls_velocity = Point(-10, 1)
      #       balls.set_velocity(balls_velocity)
      #       self._audio_service.play_sound(constants.SOUND_BOUNCE)
      #       bricks.remove(brick)
         