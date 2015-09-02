__author__ = 'vladimir'

from __exceptions__.MainError import MainError


class BrokenLineError(MainError):

    def __init__(self):
        super(BrokenLineError, self).__init__("*** Broken Line error occurred. ***")

    def return_err_message(self, message):
        return super(BrokenLineError, self).return_err_message(message)



