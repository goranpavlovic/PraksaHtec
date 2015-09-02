__author__ = 'vladimir'

import math

class A:

    @classmethod
    def func_one(cls):
        print("Test")


A.field = 50

for i in range(0, 10):
    print(A().field)


A().func_one()


def magic_num(self, a):
    p = a
    result = 0
    d = 0
    list_ = []
    while a > 0:
        list_.append(a-(a/10)*10)
        d = a/10
        a = d
    for item in list_:
        result += math.pow(item, len(list_))
    if result == a:
        print("Number %d is magic" % p)
    else:
        print("Number %d is not magic" % p)


A.func_one = magic_num
A().func_one(365)

#
# #A.method_1 = lambda p: print "Hi %d" % p
#
# A().method_1()

