__author__ = 'vladimir'


def binary_search(a, key):
    low = 0
    high = len(a) - 1
    while low < high:
        mid = (low + high) / 2
        if a[mid] == key:
            return mid
        else:
            if a[mid] > key:
                high = mid - 1
            else:
                low = mid + 1
    print("This list has no element", key)
    print(mid)


def open_file():
    with open('message.txt', 'r') as input_:
        with open('message_.txt', 'w') as output_:
            for item in input_:
                output_.write(item.upper())


def enum_func(a):
    for index, item in enumerate(a):
        print(index, item)
        with open('message_.txt', 'a') as input_:
            input_.write(str(index))
            input_.write('\t')
            input_.write(str(item))
            input_.write('\n')


def max_func(a):
    _max_ = a[0]
    for item in range(1, len(a)):
        if a[item] > _max_:
            _max_ = a[item]
    return _max_


def min_func(a):
    _min_ = a[0]
    for item in range(1, len(a)):
        if a[item] < _min_:
            _min_ = a[item]
    return _min_


def min_max_func(a, b):
    return min_func(a), max_func(b)


def argument_func(a, *args, **kwargs):
    print('Normal argument', a)
    print('Argument list', args)
    print('Keyword argument', kwargs)


def my_keyword_argument(*args, **kwargs):
    for item in kwargs.keys():
        print('key is: ', item, 'value is: ', kwargs[item])


def my_keyword_argument2(test1, *args):
    for item in args:
        print('key is: ', item)


def my_keyword_argument3(**kwargs):
    for item in kwargs.keys():
        print('key is: ', item, 'value is: ', kwargs[item])
