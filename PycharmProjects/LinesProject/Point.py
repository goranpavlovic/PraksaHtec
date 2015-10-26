__author__ = 'Vlada'

from __exceptions__.PointError import PointError
from __exceptions__.MainError import MainError

import math


class Point(object):

    #point_flag = False

    def __init__(self, x=0, y=0):
        try:
            if x > 100 or y > 100:
                raise PointError()
            self.x = x
            self.y = y
        except PointError as pe:
            print(pe.return_err_message("Coordinates outside scope. "))
            self.reset_coordinates()
        finally:
            pass
            # print("point finally block executed")

    def reset_coordinates(self):
        self.x = 0
        self.y = 0

    def set_x(self, x_):
        try:
            if x_ > 100:
                raise PointError()
            self.x = x_
        except PointError as pe:
            print(pe.return_err_message("Coordinates outside scope. "))
        finally:
            pass

    def set_y(self, y_):
        try:
            if y_ > 100:
                raise PointError()
            self.x = y_
        except PointError as pe:
            print(pe.return_err_message("Coordinates outside scope. "))
        finally:
            pass

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # @property
    # def x(self):
    #     return self.x
    #
    # @property
    # def y(self):
    #     return self.y
    #
    # @x.setter
    # def x(self, value):
    #     self.x = value
    #
    # @y.setter
    # def y(self, value):
    #     self.y = value
    #

    def get_point(self):
        return self.x,  self.y

    def print_point(self):
        print("Coordinates (%d,%d)" % (self.x, self.y))

    def distance_coord(self, x_, y_):
        try:
            if x_ > 100 or y_ > 100:
                raise PointError()
        except PointError as pe:
            print(pe.return_err_message("Coordinates outside scope. "))
        finally:
            pass

        return math.sqrt(math.pow(self.x - x_, 2) + math.pow(self.y - y_, 2))

    def distance_point(self, point):
        try:
            if point.x > 100 or point.y > 100:
                raise PointError()
        except PointError as pe:
            print(pe.return_err_message())
        finally:
            pass

        return math.sqrt(math.pow(self.x - point.x, 2) + math.pow(self.y - point.y, 2))

    # Here we practice static methods, now we don't call these methods with the Point object,
    # but we pass a coordinates or the Point objects as arguments of these static functions
    @staticmethod
    def distance_coord__(x, y, x_, y_):
        return math.sqrt(math.pow(x - x_, 2) + math.pow(y - y_, 2))

    @staticmethod
    def distance_point__(point_, point):
        return math.sqrt(math.pow(point_.x - point.x, 2) + math.pow(point_.y - point.y, 2))

    @staticmethod
    def print_array_of_points(array_):
        for item in range(0, len(array_)):
            array_[item].print_point()




