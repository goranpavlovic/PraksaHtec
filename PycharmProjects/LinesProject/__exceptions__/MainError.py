__author__ = 'vladimir'

from abc import ABCMeta


class MainError(Exception):

    __metaclass__ = ABCMeta

    def __init__(self, message="ERROR"):
        self.message = message

    def return_err_message(self, message):
        return "Exception: %s %s" % (self.message, message)










