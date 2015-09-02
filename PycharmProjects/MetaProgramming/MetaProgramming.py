__author__ = 'Vlada'


def class_with_method(args):
    class A:
        def __init__(self, name="MetaClass"):
            self.name = name

        def get_name(self):
            return self.name

        def print_name(self):
            print("Name of this class is %s" % self.get_name())
    for item in args:
        setattr(A, item.__name__, item)
    return A


def say_something(self):
    print("Meta-programming, Python my new LOVE")


def meta_pro_func(self):
    print("We try to make class with more than one method")


def factorial(self, n):
    result = 1
    for i in range(1, n+1):
        result *= i
    print("Number %d factorial is %d" % (n, result))

# Define a list of class functions, then we pass that list
# as argument in function class_with_method
list_method = [say_something, meta_pro_func, factorial]

B = class_with_method(list_method)

b = B()

b.say_something()
b.meta_pro_func()
b.factorial(5)
b.print_name()




