__author__ = 'vladimir'

from abc import ABCMeta, abstractmethod


class Subscriber(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def notify(self):
        pass


