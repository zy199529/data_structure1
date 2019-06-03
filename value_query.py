#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-06-03 09:11:44
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-06-03 09:34:07


def value_query(A, value):
    rows = len(A)
    cols = len(A[0])
    if rows > 0 and cols > 0:
        row = 0
        col = cols-1
        while row < rows and col > 0:
            if value == A[row][col]:
                return True
            elif value < A[row][col]:
                col = col-1
            else:
                row = row+1
    return False
A = [[1, 2, 8, 9],
     [2, 4, 9, 12],
     [4, 7, 10, 13],
     [6, 8, 11, 15]]
print(value_query(A, 5))
