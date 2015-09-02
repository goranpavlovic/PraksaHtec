__author__ = 'Vlada'

from Line import Line
from Point import Point
from StraightLine import StraightLine


# Class BrokenLine extends Line
#
class BrokenLine(Line):

    def __init__(self, array):
        super(BrokenLine, self).__init__()
        self.array = array

    def line_length(self):
        length = 0
        for item in range(0, len(self.array) - 1):
            length += StraightLine(self.array[item], self.array[item + 1]).line_length()
        return length

    def print_line(self):
        super(BrokenLine, self).print_line()
        print("[broken line:")
        Point.print_array_of_points(self.array)
        print("]")




