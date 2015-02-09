#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import numpy as np


def main():
    A = np.array([[3,6,1],[2,5,7],[5,8,1]])  # matrix
    print("A:")
    print(A)

    B = np.array([[6,2,7],[5,2,5],[4,8,9]])  # matrix
    print("B:")
    print(B)

    v = np.array([1,2,3])  # vector
    print("v:")
    print(v)

    print("AB:")
    print(np.dot(A, B)) # AB

    print("Av:")
    print(np.dot(A, v))  # Av

    print("A transpose:")
    print(A.T)  # transpose

    print("A inverse:")
    print(np.linalg.inv(A))  # inverse


if __name__ == '__main__':
    main()
