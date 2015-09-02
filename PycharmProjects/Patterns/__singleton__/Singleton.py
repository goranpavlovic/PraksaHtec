__author__ = 'vladimir'

from abc import abstractmethod


# Design pattern SINGLETON class, for example symbol table during compiling program
class Table(object):

    instance = None

    def __init__(self, sym_type, name, description, bind):
        self.type = sym_type
        self.name = name
        self.description = description
        self.bind = bind

    @staticmethod
    def instance():
        if not Table.instance:
            Table.instance = Table()
        return Table.instance

    @abstractmethod
    def some_operation(self):
        pass



