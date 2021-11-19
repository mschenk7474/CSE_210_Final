import sys
from game.point import Point
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        pass
        
    def get_direction_left(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0
        #PUT IN FIRST PLAYERS!!

        #Second Player's controls
        if self.is_w_pressed():
            dy = -1
        
        if self.is_s_pressed():
            dy = 1

        direction = Point(dx, dy)
        return direction

    def get_direction_right(self):
        """Gets the selected direction based on the currently pressed keys.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if self.is_up_pressed():
            dy = -1
        
        if self.is_down_pressed():
            dy = 1

        direction = Point(dx, dy)
        return direction

    def is_up_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_UP)

    def is_down_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_DOWN)

    def is_w_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_W)

    def is_s_pressed(self):
        return raylibpy.is_key_down(raylibpy.KEY_S)


    def window_should_close(self):
        return raylibpy.window_should_close()