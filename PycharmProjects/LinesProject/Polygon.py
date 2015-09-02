__author__ = 'Vlada'

from Point import Point
from BrokenLine import BrokenLine
from StraightLine import StraightLine


# Class Polygon extends BrokenLine
#
class Polygon(BrokenLine):

    def __init__(self, array):
        super(Polygon, self).__init__(array)

    def line_length(self):
        first = self.array[0]
        last = self.array[len(self.array) - 1]
        first_last = StraightLine(first, last).line_length()
        return super(Polygon, self).line_length() + first_last

    def print_polygon(self):
        print("Polygon %d :" % super(Polygon, self).get_id())
        Point.print_array_of_points(self.array)


