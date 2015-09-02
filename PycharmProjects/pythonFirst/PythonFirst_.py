__author__ = 'vladimir'

# from __functions__ import binary_search as search
from __functions__ import open_file as openf
from __functions__ import enum_func as efunc
from __functions__ import min_max_func as mm_func
from __functions__ import *
from __classes__ import *

#
# # Creating list
# a = []
#
# # Appending elements in list
# for i in range(1, 10000, 3):
#     a.append(i)
# print(a)
#
# position = search(a, 10)
#
# print(position)

# openf()
#
# a = ['house', 'apple', 'peach', 'dreiser']
#
# efunc(a)

# x = [45, 74, 65, 12, 89, 16]
# y = [37, 18, 36, 29, 55, 12, 103]
#
# a, b = mm_func(x, y)
#
# print('Minimum of first list is', a)
# print('Maximum of second list is', b)

# argument_func(10, ('Vladimir', 'Alexander'), peter=500)

dictionary = {'apple' : 'two apples', 'apples' : 'four apples'}

my_list = ("test1", "test2", "test3")
#
# # dictionary.update()
# # dictionary.update()
#

dictionary.update({'test1': 'test2'})
dictionary.update({'apples': 'something new'})

print "-------- new call------------"
my_keyword_argument(arg1="test1", arg2="test2", arg3="test3")

print "-------- new call------------"
my_keyword_argument("test1", "test2", "test3")

print "-------- new call------------"
my_keyword_argument2("test1", "test2", "test3")

print "-------- new call------------"
my_keyword_argument2(*my_list)

print "-------- new call------------"
my_keyword_argument3(arg1="test1", arg2="test2", arg3="test3")

print "-------- new call------------"
my_keyword_argument3(**dictionary)

"""
point_1 = Point(5, 6)
point_2 = Point(8, 10)

distance = point_1.distance(point_2)

print('Distance between point_1 and point_2 is', distance)

# Change of first point
print('Before changes ')
point_1.print_x()
point_1.print_y()

print('Set coordinates of first point')
point_1.set_x(17)
point_1.set_y(12)

print('After changes')
point_1.print_x()
point_1.print_y()

distance = point_1.distance(point_2)

print('Distance between point_1 and point_2 is', distance)

# Change of second point
print('Before changes ')
point_2.print_x()
point_2.print_y()

print('Set coordinates of second point')
point_2.set_x(15)
point_2.set_y(20)

print('After changes')
point_2.print_x()
point_2.print_y()

distance = point_1.distance(point_2)

print('Distance between point_1 and point_2 is', distance)
"""

class MyException(Exception):

    message2 = ''

    def __init__(self, message):
        self.message = message

class A(object):
    def __init__(self):
        pass

    def some_fn(self):
        raise MyException("--------Exception happends----")

class B(object):

    def __init__(self):
        self.a_object = None

    def initialize_a(self):
        try:
            object_a = A()
            object_a.some_fn()
        except MyException as e:
            print "------------my exception----------"
        except Exception as e:
            print "------------exception-------------"
        finally:
            print "------------finally block---------"


object = B()
object.initialize_a()














