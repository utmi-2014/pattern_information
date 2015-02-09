#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import numpy as np


def load_data(filename):
    data = []
    with open(filename, 'rb') as f:
        for row in f.readlines():
            # firstly, row is like '  1.6191290e+000  4.0366157e+000\r'
            # row.strip() returns '1.6191290e+000  4.0366157e+000'
            # row.strip().split() returns ['1.6191290e+000', '4.0366157e+000']
            # map(float, row.strip().split()) returns [1.619129, 4.0366157]
            row = map(float, row.strip().split())
            data.append(row)
    return np.array(data)


def main():
    print("with load_data function:")
    data = load_data('data.txt')
    print(data)

    # acutually upper is same as np.loadtxt('data.txt')
    print("with numpy.loadtxt function:")
    data = np.loadtxt('data.txt')
    print(data)


if __name__ == '__main__':
    main()
