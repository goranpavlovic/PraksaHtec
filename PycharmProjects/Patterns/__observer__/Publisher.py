__author__ = 'vladimir'

from abc import ABCMeta, abstractmethod


class Publisher(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def unregister(self):
        pass

    @abstractmethod
    def notify_all(self):
        pass



