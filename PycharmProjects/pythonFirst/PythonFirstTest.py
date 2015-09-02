__author__ = 'vladimir'

from __classes__ import *

# Creating two points
point_1 = Point(10, 20)
point_2 = Point(6, 7)

# Creating line
line_1 = Line(point_1, point_2)

line_1.print_line()

print("---------------- NEW STATEMENT ------------------")

print("Line length is ", line_1.line_len())

print("---------------- NEW STATEMENT ------------------")

point_1.set_x(8)
point_1.set_y(17)

point_2.set_x(52)
point_2.set_y(37)

line_1.set_first_point(point_1)
line_1.set_second_point(point_2)

line_1.print_line()

print("---------------- NEW STATEMENT ------------------")

print("Line length is ", line_1.line_len())

print("---------------- NEW STATEMENT ------------------")


