__author__ = 'Vlada'

from Point import Point
from StraightLine import StraightLine
from BrokenLine import BrokenLine
from Polygon import Polygon


print("------------------ CLASS Point TESTING ------------------")

p1 = Point(10, 20)
p2 = Point(15, 25)
p3 = Point(11, 5)
p4 = Point(8, 0)

print("Point p1(%d,%d):" % (p1.get_x(), p1.get_y()))
print("Point p2(%d,%d):" % (p2.get_x(), p2.get_y()))
print("Point p3(%d,%d):" % (p3.get_x(), p3.get_y()))
print("Point p4(%d,%d):" % (p4.get_x(), p4.get_y()))

p1.print_point()
p2.print_point()
p3.print_point()
p4.print_point()

print("Distance between points p1 and (4, 12) is", p1.distance_coord(4, 12))
print("Distance between points (5, 7) and (4, 7)", Point.distance_coord__(5, 7, 4, 7))
print("Distance between points p3 and p4 is %d " % p3.distance_point(p4))
print("Distance between points p1 and p2 is %d " % Point.distance_point__(p1, p2))

p1.set_x(0)
p1.set_y(0)
p2.set_x(1)
p2.set_y(1)
p3.set_x(2)
p3.set_y(2)
p4.set_x(3)
p4.set_y(3)

points = [p1, p2, p3, p4]

Point.print_array_of_points(points)

print("------------------ CLASS Line TESTING ------------------")

# l1 = Line()

print("------------------ CLASS StraightLine TESTING ------------------")

sl1 = StraightLine()
sl2 = StraightLine(p1, p2)
sl3 = StraightLine(Point(0, 0), p3)

print("Straight line sl1 length is %d" % sl1.line_length())
print("Straight line sl2 length is %d" % sl2.line_length())

sl1.print_straight_line()
sl2.print_straight_line()
sl3.print_straight_line()

print("------------------ CLASS BrokenLine TESTING ------------------")

bl = BrokenLine(points)
print("Broken line length is %d " % bl.line_length())
bl.print_line()

print("------------------ CLASS Polygon TESTING ------------------")

pp1 = Point(3, 7)
pp2 = Point(7, 1)
pp3 = Point(8, 4)
pp4 = Point(11, 0)

points_1 = [pp1, pp2, pp3, pp4]

pol = Polygon(points_1)

print("Polygon length is %d " % pol.line_length())


print("---------------------- CLASS Point TESTING EXCEPTIONS -----------------------")
# p1 = Point(415, 21)
# p2 = Point(12, 10)
#
# p1.set_x(102)
# p2.set_y(152)
#
# xc = p1.get_x()
# yc = p1.get_y()
#
# print("======================================================================")
#
# xb = p2.get_x()
# yb = p2.get_y()
#
# print("======================================================================")
#
# t1 = p1.get_point()
# t2 = p2.get_point()
#
# print("======================================================================")
#
# p1.print_point()
# p2.print_point()
#
# print("======================================================================")
#
# p1.distance_coord(55, 177)
# p1.distance_point(Point(100, 101))
# p2.distance_coord(55, 177)
# p2.distance_point(Point(100, 101))
#
# print("======================================================================")
#
# p1.set_x(10)
# p2.set_y(14)
#
# xc = p1.get_x()
# yc = p1.get_y()
#
# print("======================================================================")
#
# xb = p2.get_x()
# yb = p2.get_y()
#
# print("======================================================================")
#
# t1 = p1.get_point()
# t2 = p2.get_point()
#
# print("======================================================================")
#
# p1.print_point()
# p2.print_point()
#
# print("======================================================================")
#
# p1.distance_coord(55, 177)
# p1.distance_point(Point(100, 101))
# p2.distance_coord(55, 177)
# p2.distance_point(Point(100, 101))
#
# print("======================================================================")

print("---------------------- CLASS StraightLine TESTING EXCEPTIONS -----------------------")

tp1 = Point(120, 123)
tp2 = Point(110, 45)

print("-----------success point test---------")
ppp1 = Point(1, 2)
ppp2 = Point(20, 30)
ppl = StraightLine(ppp1, ppp2)
print("Line pp length is %d " % ppl.line_length())





