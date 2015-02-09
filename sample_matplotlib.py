#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import numpy as np
import matplotlib.pyplot as plt


def main():
    x = [1,2,3,4,5,6,7,8,9,10]
    y1 = np.random.random(10)
    y2 = np.random.random(10)

    plt.scatter(x, y1, color="b")
    plt.scatter(x, y2, color="r")
    plt.savefig("sample_matplotlib.png")


if __name__ == '__main__':
    main()