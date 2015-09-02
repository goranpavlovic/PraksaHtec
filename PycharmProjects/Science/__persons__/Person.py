__author__ = 'vladimir'

from  abc import ABCMeta


class Person(object):

    __metaclass__ = ABCMeta

    def __init__(self, name="Person"):
        self.name = name

    def get_name(self):
        return self.name


