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
      ball = cast["ball"][0] #There's only one ball
      ball_x = ball._position.get_x()
      ball_y = ball._position.get_y()
      ball_velocity = ball.get_velocity()
      ball_velocity_x = ball._velocity._x
      ball_velocity_y = ball._velocity._y

      # If it hits top or bottom of the screen
      if ball_x == 0:
         ball_velocity_x = ball_velocity_x * -1
         ball_velocity = Point(ball_velocity_x,ball_velocity_y)
         ball.set_velocity(ball_velocity)
      elif ball_x == 800:
         ball_velocity_x = ball_velocity_x * -1
         ball_velocity = Point(ball_velocity_x,ball_velocity_y)
         ball.set_velocity(ball_velocity)

      #If it hits left or right of the screen
      if ball_y == 0:
         ball_velocity_y = ball_velocity_y * -1
         ball_velocity = Point(ball_velocity_x,ball_velocity_y)
         ball.set_velocity(ball_velocity)
      elif ball_y == 600:
         ball_velocity_y = ball_velocity_y * -1
         ball_velocity = Point(ball_velocity_x,ball_velocity_y)
         ball.set_velocity(ball_velocity)

      #Paddle Stuff
      paddleL = cast["paddleL"][0]
      paddleL_x = paddleL._position.get_x()
      paddleL_y = paddleL._position.get_y()
      paddleL_dx = paddleL._velocity._x
      paddleL_dy = paddleL._velocity._y
      paddleL_height = self.constants.PADDLE_HEIGHT
      max_y = self.constants.MAX_Y
      paddleL_y_bound = max_y + paddleL_height 

      paddleR = cast["paddleR"][0]
      paddleR_x = paddleR._position.get_x()
      paddleR_y = paddleR._position.get_y()
      paddleR_dx = paddleR._velocity._x
      paddleR_dy = paddleR._velocity._y
      paddleR_height = self.constants.PADDLE_HEIGHT
      max_y = self.constants.MAX_Y
      paddleR_y_bound = max_y + paddleR_height


      if paddleL_y == 0:
         paddleL_y_new = max(paddleL_y - paddleL_dy, 0)
         paddleL_position = Point(paddleL_x, paddleL_y_new)
         paddleL.set_position(paddleL_position)
      elif paddleL_y == 600:
         paddleL_y_new = min(paddleL_y - paddleL_dy, paddleL_y_bound ) #was 735
         paddleL_position = Point(paddleL_x, paddleL_y_new)
         paddleL.set_position(paddleL_position)
      elif paddleR_y == 0:
         paddleR_y_new = max(paddleR_y - paddleR_dy, 0)
         paddleR_position = Point(paddleR_x, paddleR_y_new)
         paddleR.set_position(paddleR_position)
      elif paddleR_y == 600:
         paddleR_y_new = min(paddleR_y - paddleR_dy, paddleR_y_bound ) #was 735
         paddleR_position = Point(paddleR_x, paddleR_y_new)
         paddleR.set_position(paddleR_position)


      # ball = cast["balls"][0] #There's only one ball
      # ball_x = ball._position.get_x()
      # ball_y = ball._position.get_y()
      # ball_velocity = ball.get_velocity()
      # ball_velocity_x = ball._velocity._x
      # ball_velocity_y = ball._velocity._y
      # ball_list = cast["balls"]
      # if ball_x == 0:
      #    ball_velocity_x = ball_velocity_x * -1
      #    ball_velocity = Point(ball_velocity_x,ball_velocity_y)
      #    ball.set_velocity(ball_velocity)
      # elif ball_x == 800: #was 750
      #    ball_velocity_x = ball_velocity_x * -1
      #    ball_velocity = Point(ball_velocity_x,ball_velocity_y)
      #    ball.set_velocity(ball_velocity)
      
      # #Paddle Stuff
      # paddle = cast["paddle"][0]
      # paddle_x = paddle._position.get_x()
      # paddle_y = paddle._position.get_y()
      # paddle_dx = paddle._velocity._x
      # paddle_width = self.constants.PADDLE_WIDTH
      # max_x = self.constants.MAX_X
      # paddle_x_bound = max_x + paddle_width
      # if paddle_x == 0:
      #    paddle_x_new = max(paddle_x - paddle_dx, 0)
      #    paddle_position = Point(paddle_x_new, paddle_y)
      #    paddle.set_position(paddle_position)
      # elif paddle_x == 750: #was 750
      #    paddle_x_new_2 = min(paddle_x - paddle_dx, paddle_x_bound ) #was 735
      #    paddle_position = Point(paddle_x_new_2, paddle_y)
      #    paddle.set_position(paddle_position)