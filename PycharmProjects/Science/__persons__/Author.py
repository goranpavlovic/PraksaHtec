__author__ = 'vladimir'

from __persons__.Person import Person


class Author(Person):

    def __init__(self, name):
        super(Author, self).__init__(name)

    def write(self, title):
        pass

