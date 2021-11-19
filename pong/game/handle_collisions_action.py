from game.actor import Actor
from game.point import Point
from game.action import Action
from game import constants
from game.audio_service import AudioService

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
         