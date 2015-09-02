__author__ = 'vladimir'

import math


#  Simulate Point in 2D
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_x(self):
        print('Coordinate x is: %d' % self.x)

    def print_y(self):
        print('Coordinate y is: %d' % self.y)

    def print_point(self):
        print('Point is (%d, %d)' % (self.x, self.y))

    def set_x(self, x_):
        self.x = x_

    def set_y(self, y_):
        self.y = y_

    def get_point(self):
        return self.x, self.y

    def distance(self, point):
        return math.sqrt(math.pow(self.x - point.x, 2) + math.pow(self.y - point.y, 2))


# Simulate closed line
# members of this class are Point type


class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def line_len(self):
        return self.p1.distance(self.p2)

    def move_first_point(self, x_, y_):
        self.p1.x = x_
        self.p1.y = y_

    def move_second_point(self, x_, y_):
        self.p2.x = x_
        self.p2.y = y_

    def set_first_point(self, p1_):
        self.p1 = p1_

    def set_second_point(self, p2_):
        self.p2 = p2_

    def print_line(self):
        print("First point of this line is", self.p1.get_point(),
              ". Second point of this is", self.p2.get_point())



