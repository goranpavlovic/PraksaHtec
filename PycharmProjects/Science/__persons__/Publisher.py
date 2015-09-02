__author__ = 'vladimir'

from __persons__.Person import Person


class Publisher(Person):

    def __init__(self, name):
        super(Publisher, self).__init__(name)

    def publish(self, collection, number):
        pass

    def hire(self, redactor):
        pass

    def release(self, redactor):
        pass