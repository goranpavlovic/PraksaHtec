__author__ = 'Vlada'

import math

from Line import Line
from Point import Point
from __exceptions__.StraightLineError import StraightLineError


# Class StraightLine extends class Line
#
class StraightLine(Line):

    def __init__(self, a=Point(-1, -1), b=Point(1, 1)):
        super(StraightLine, self).__init__()
        self.a = a
        self.b = b

    def line_len_solve(self):
        diff_x = self.a.get_x() - self.b.get_x()
        diff_y = self.a.get_y() - self.b.get_y()
        result = math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))

        if result > 10:
            raise StraightLineError()

        return result

    def line_length(self):
        result = 0
        try:
            result = self.line_len_solve()
        except StraightLineError as sle:
            print(sle.return_err_message("Line too long. "))
        finally:
            pass

        return result

    def print_straight_line(self):
        self.print_line()
        print("[duz: A", self.a.get_point(), 'B', self.b.get_point(), ']')


