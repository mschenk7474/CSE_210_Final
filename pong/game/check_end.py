class CheckEnd():
   """
   This class has the game_done condtions, which basically determine
   when the game is done.
   """
   def __init__(self, cast):
      self._cast = cast
      self._keep_playing = True
   def execute(self, cast):
      """
      If anything needs to be executed for the condtions to work, it is done here.
      """
      pass
      # ball = cast["balls"][0] #There's only one ball
      # ball_list = cast["balls"]
      # ball_y = ball._position.get_y()

      # if ball_y >= 575:
      #    for ball in ball_list:
      #       ball_list.remove(ball)
      # pass

   def if_done(self):
      """
      Has the game done condtions.
      """
      pass
      # if len(self._cast["bricks"]) == 0:
      #           # Game over
      #    return False
      # elif len(self._cast["balls"]) == 0:
      #           # Game over
      #    return False
      # else:
      #    return True