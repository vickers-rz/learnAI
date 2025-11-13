# def double(x):
#     return x * 2
#
# def triple(x):
#     return x * 3
#
# def calc_number(func, x):
#     return func(x)
#
# print(double(3))
# print(triple(3))
# print(calc_number(double, 3))
# print(calc_number(triple, 3))


def get_multiple_func(n):
    def multiple(x):
        return n ** x

    return multiple

square = get_multiple_func(2)
triple = get_multiple_func(3)

print(square(3))
print(triple(3))

import numpy as np

import matplotlib.pyplot as plt






