import random
from game import constants
from game.actor import Actor
from game.point import Point

class ScoreBoard(Actor):
    """Points earned. The responsibility of the ScoreBoard is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        self._points_left = 0
        self._points_right = 0
        self._scoreboard_left = []
        self._scoreboard_right = []
        # position = Point(1, 0)
        # self.set_position(position)
        # self.set_text(f"Score: {self._points}")
    
    def set_scoreboard_left(self):
        """
        Sets the scoreboard left as an actor and gives it properties.
        """
        scoreL = Actor()
        scoreL_position = Point(250, 0)
        scoreL.set_position(scoreL_position)
        scoreL.set_text(f"{self._points_left}")

        self._scoreboard_left.append(scoreL)
    
    def get_scoreboard_left(self):
        """
        Returns the scoreboard left to be used elsewhere.
        """
        return self._scoreboard_left

    def set_scoreboard_right(self):
        """
        Sets the scoreboard right as an actor and gives it properties.
        """
        scoreR = Actor()
        scoreR_position = Point(500, 0)
        scoreR.set_position(scoreR_position)
        scoreR.set_text(f"{self._points_left}")

        self._scoreboard_right.append(scoreR)
    
    def get_scoreboard_right(self):
        """
        Returns the scoreboard right to be used elsewhere.
        """
        return self._scoreboard_right

    def add_points_left(self, points):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        scoreL = self._scoreboard_left[0]
        self._points_left += points
        scoreL.set_text(f"{self._points_left}")

    def add_points_right(self, points):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        scoreR = self._scoreboard_right[0]
        self._points_right += points
        scoreR.set_text(f"{self._points_right}")