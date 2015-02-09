#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import numpy as np
import matplotlib.pyplot as plt


def main():
    x = [1,2,3,4,5,6,7,8,9,10]
    y1 = np.random.random(10)
    y2 = np.random.random(10)

    plt.scatter(x, y1, color="r")  # 散布図, 赤で
    plt.plot(x, y2, color="b")  # 折れ線図, 青で
    plt.savefig("sample_matplotlib.png")  # グラフを保存
                                          # 表示したい場合はplt.show()


if __name__ == '__main__':
    main()