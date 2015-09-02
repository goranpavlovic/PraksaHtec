__author__ = 'vladimir'

from __exceptions__.MainError import MainError


class PolygonError(MainError):

    def __init__(self):
        super(PolygonError, self).__init__("*** Polygon error occurred. ***")

    def return_err_message(self, message):
        return super(PolygonError, self).return_err_message(message)


