__author__ = 'vladimir'

from __exceptions__.MainError import MainError


class StraightLineError(MainError):

    def __init__(self):
        super(StraightLineError, self).__init__("*** Straight line error occurred. ***")

    def return_err_message(self, message):
        return super(StraightLineError, self).return_err_message(message)


