__author__ = 'vladimir'

from __exceptions__.MainError import MainError


class PointError(MainError):

    def __init__(self):
        super(PointError, self).__init__("*** Point error occurred. ***")

    def return_err_message(self, message):
        return super(PointError, self).return_err_message(message)

