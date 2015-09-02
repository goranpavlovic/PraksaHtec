__author__ = 'Vlada'

from abc import ABCMeta, abstractmethod


# This class is declared as abstract
#
class Line(object):
    __metaclass__ = ABCMeta  # Metaclass for defining Abstract Base Classes

    # All variables declared outside class constructor are static,
    # and we access to these variables with or without class instance
    lastID = 0

    # In Python, also, we can't make instance(object) of abstract class,
    # but we'll inherit non-static members of superclass in subclass
    # @abstractmethod
    def __init__(self):
        self.id = Line.lastID + 1

    @abstractmethod
    def line_length(self):
        pass

    def get_id(self):
        return self.id

    def print_line(self):
        print("Line id is %d" % self.id)


