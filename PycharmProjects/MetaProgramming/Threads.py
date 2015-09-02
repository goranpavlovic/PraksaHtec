__author__ = 'vladimir'

import numpy as np
import scipy as sc

import matplotlib.pyplot as pyplot


# n = 1024
# X = np.linspace(-2*np.pi, 2*np.pi, n, endpoint=True)
# Y2 = np.sin(X)
# Y1 = np.cos(X)
#
# # f1 = pyplot.figure()
# pyplot.plot(X, Y1, color='blue', alpha=1.00)
# pyplot.plot(X, Y2, color='red', alpha=1.00)
# pyplot.show()
# pyplot.savefig('foo.png')

# import pylab as pl
# import numpy as np
#
# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# C, S = np.cos(X), np.sin(X)
#
# pl.plot(X, C)
# pl.plot(X, S)
#
# pl.show()
# pl.savefig('foo.png')


# AX = B
# 5x - 6y + 7y = 15
# -7x - 2y + 3z = -16
# 4x + 7y + z = 18

# A = np.matrix([[5, -6, 7], [-7, -2, 3], [4, 7, 1]])
# B = np.matrix([[15], [-16], [18]])
#
# X = A ** (-1) * B
#
# print(X)
#
#
# class Matrix(object):
#
#     def __init__(self, a, b):
#         try:
#             if a.shape[1] != b.shape[0]:
#                 raise Exception()
#             self.a = a
#             self.b = b
#         except Exception as ex:
#             print("Dimensions of matrix are not compatible")
#         finally:
#             pass
#
#     def set_a(self, a):
#         self.a = a
#
#     def get_a(self):
#         return self.a
#
#     def set_b(self, b):
#         self.b = b
#
#     def get_b(self):
#         return self.b
#
#     def get_dimension_a(self):
#         return self.a.shape[0], self.a.shape[1]
#
#     def get_dimension_b(self):
#         return self.b.shape[0], self.b.shape[1]
#
#     def add(self):
#         print("Matrix A + B is", self.a + self.b)
#         return self.a + self.b
#
#     def sub(self):
#         print("Matrix A - B is", self.a - self.b)
#         return self.a - self.b
#
#     def mul(self):
#         print("Matrix A * B is", self.a * self.b)
#         return self.a * self.b
#
#     def det_a(self):
#         print("Determinant of matrix A is %d" % np.linalg.det(self.a))
#         return np.linalg.det(self.a)
#
#     def det_b(self):
#         print("Determinant of matrix B is %d" % np.linalg.det(self.b))
#         return np.linalg.det(self.b)
#
# M1 = np.matrix([[4, 5, 15], [-9, 7, 14], [7, -9, 11]])
# M2 = np.matrix([[-4, 15, -7], [-6, 12, -17], [1, -6, 0]])
#
# matrix = Matrix(M1, M2)
#
# matrix.add()
# matrix.sub()
# matrix.mul()
# matrix.det_a()
# matrix.det_b()
#
# m, n = matrix.get_dimension_a()
#
# print("Dimensions of matrix M1 are (%d, %d)" % (m, n))












