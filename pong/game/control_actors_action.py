from game.actor import Actor
from game.point import Point
from game import constants
from game.action import Action

class ControlActorsAction():
    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors. For this case, 
        it will be moving the paddles.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
      #   direction = self._input_service.get_direction()
      #   paddle = cast["paddle"][0] # there's only one in the cast
      #   paddle.set_velocity(direction.scale(constants.PADDLE_SPEED))
        #Left Paddle
        direction_left = self._input_service.get_direction_left()
        paddleL = cast["paddleL"][0]
        paddleL.set_velocity(direction_left.scale(constants.PADDLE_SPEED))


        #Right Paddle
        direction_right = self._input_service.get_direction_right()
        paddleR = cast["paddleR"][0]
        paddleR.set_velocity(direction_right.scale(constants.PADDLE_SPEED))