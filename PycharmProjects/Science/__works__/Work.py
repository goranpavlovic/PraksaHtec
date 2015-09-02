__author__ = 'vladimir'

from abc import ABCMeta, abstractmethod


class Work(object):

    __metaclass__ = ABCMeta

    last_id = 0

    def __init__(self, title, authors):
        self.title = title
        self.authors = authors
        self.id = Work.last_id + 1

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_authors(self):
        return self.authors

    def put_in(self, area):
        pass

    @abstractmethod
    def copy(self):
        pass

