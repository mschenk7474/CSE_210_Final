from game.score_board import ScoreBoard
from game.point import Point
from game import constants
from game.ball import Ball


class CheckEnd():
   """
   This class has the game_done condtions, which basically determine
   when the game is done.
   """
   def __init__(self, cast):
      self._cast = cast
      self._keep_playing = True
      self.score_board = ScoreBoard()
      self.b = Ball()
   def execute(self, cast):
      """
      If anything needs to be executed for the condtions to work, it is done here.
      """
      pass
      ball = cast["ball"][0] #There's only one ball
      ball_list = cast["ball"]
      # ball_list = cast["balls"]
      score_board_left = cast["scoreboardL"][0]
      score_board_right = cast["scoreboardR"][0]
      ball_y = ball._position.get_y()
      ball_x = ball._position.get_x()
      self.score_left = 0
      self.score_right = 0
      center_x = constants.MAX_X / 2
      center_y = constants.MAX_Y / 2
      if ball_x == 0:
         #Add points
         self.score_left = self.score_left + 1
         sbl_text = score_board_left.get_text()
         sbl_text = (f"{self.score_left}")
         score_board_left.set_text(sbl_text)
         #self.score_board.add_points_left(score_left)
         #Put the ball back in the middle
         # for ball in ball_list:
         #    ball_list.remove(ball)
         # self.b.set_ball()

         ball_x = center_x
         ball_y = center_y
         ball_position = Point(ball_x, ball_y)
         ball.set_position(ball_position)
      elif ball_x == 800:
         self.score_right = self.score_right + 1
         sbl_text_r = score_board_right.get_text()
         sbl_text_r = (f"{self.score_right}")
         score_board_right.set_text(sbl_text_r)
         #self.score_board.add_points_right(score_right)
         #Put ball back in middle
         # for ball in ball_list:
         # self.b.set_ball()
         # self.b.get_ball()
         # cast["ball"] = self.b
         # ball_list.remove(ball)
         ball_x = center_x
         ball_y = center_y
         ball_position = Point(ball_x, ball_y)
         ball.set_position(ball_position)
      # if ball_y >= 575:
      #    for ball in ball_list:
      #       ball_list.remove(ball)
      # pass

   def if_done(self):
      """
      Has the game done condtions.
      """
      score_left_points = self.score_left
      score_right_points = self.score_right

      if score_left_points == 7:
         return False
      elif score_right_points == 7:
         return False
      else:
         return True
      pass
      # if len(self._cast["bricks"]) == 0:
      #           # Game over
      #    return False
      # elif len(self._cast["balls"]) == 0:
      #           # Game over
      #    return False
      # else:
      #    return True