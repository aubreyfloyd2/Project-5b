# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 2/6/2023
# Description: A class named Taxicab that has three private data members: one that holds the
#              current x-coordinate, one that holds the current y-coordinate,
#              and one that holds the current odometer reading which is able to move and update.

class Taxicab:
    """
    Represents a Taxicab moving based on x-coordinates and y-coordinates and
    the odometer reading of distance traveled.
    """
    def __init__(self, x_coord, y_coord):
        """Initializes the coordinates and the odometer to zero."""
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        """Returns the x-coordinate."""
        return self._x_coord

    def get_y_coord(self):
        """Returns the y-coordinate."""
        return self._y_coord

    def get_odometer(self):
        """Returns odometer reading of distance traveled."""
        return self._odometer

    def move_x(self, num_x):
        """How far the Taxicab should shift left or right."""
        self._num_x = num_x
        self._odometer += abs(num_x)
        self._x_coord += num_x

    def move_y(self, num_y):
        """How far the Taxicab should shift up or down."""
        self._num_y = num_y
        self._odometer += abs(num_y)
        self._y_coord += num_y

