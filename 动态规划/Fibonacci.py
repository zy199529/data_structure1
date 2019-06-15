#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-06-12 16:31:49
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-06-12 16:41:03
# 斐波那契数列 1,1,2,3,5,8,13......等等，后一个数是前两个数的和


def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = []
    for i in range(n):
        if i == 0:
            result.append(0)
        elif i == 1:
            result.append(1)
        else:
        	result.append(result[i-1]+result[i-2])
    return result
print(Fibonacci(20))

