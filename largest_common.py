#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-06-03 14:47:24
# @Last Modified by:   Lenovo
# @Last Modified time: 2019-06-03 15:37:00


def largest_common(a, b):
    lena = len(a)
    lenb = len(b)
    c = [[0 for i in range(lenb)] for j in range(lena)]
    maxNum = 0
    p = 0
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                c[i+1][j+1] = c[i][j]+1  # 对角线相加
                if c[i+1][j+1] > maxNum:
                    maxNum = c[i+1][j+1]
                    p = i+1
    return a[p-maxNum:p],maxNum
a = "abcdef"
b = "jcdeg"
c = largest_common(a,b)
print(c)