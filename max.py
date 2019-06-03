#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-05-27 19:48:42
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-05-28 23:28:24


def max_multiply(k, n):
    max = 0
    for i in range(n):
        for y in range(n):
            for j in range(n):
                if i != j | i != y | j != y:
                    if max < k[i]*k[j]*k[y]:
                        max = k[i]*k[j]*k[y]
                        print(max)
                        print(i,j,y)
    return max
if __name__ == "__main__":
    k = [1, -5, -2, 3,2]
    print(max_multiply(k, len(k)))
