#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-06-12 16:41:46
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-06-12 17:13:38
# 跳台阶问题，每次只能跳一个或两个台阶，跳到n层台阶上有几种方法
# 若第一次跳了第一阶，还剩下f(n-1)
# 若第一次跳了二阶，还剩下f(n-2)
# 一共有f(n)=f(n-1)+f(n-2)
# 斐波那契问题
# 变态跳台阶问题：一只青蛙一次可以跳上一级台阶，也可以跳上2级台阶，也可以跳上n级，
# 求该青蛙跳上n级台阶总共有多少种方法
def jump_step(n):
    if n==1:
        return 1
    result = []
    for i in range(0,n):
        if i==0:
            result.append(0)
        elif i==1:
            result.append(1)
        else:
            result.append(2*result[i-1])
    return result
print(jump_step(10))


