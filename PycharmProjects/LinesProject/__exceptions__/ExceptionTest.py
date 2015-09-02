__author__ = 'vladimir'

from __exceptions__.MainError import MainError


class A(object):

    def __init__(self):
        pass

    def test(self):
        raise MainError()


class B(object):

    def __init__(self):
        pass

    def testB(self):
        try:
            a = A()
            a.test()
        except MainError as me:
            print(me.return_err_message())
        finally:
            print(MainError().return_err_message())


print("------========= EXCEPTIONS ==========------")

B().testB()

