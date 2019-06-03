#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-06-03 15:11:30
# @Last Modified by:   Lenovo
# @Last Modified time: 2019-06-03 16:20:56
# 最长公共子序列
import numpy as np


def lcs(s1, s2):
    c = [[0 for x in range(len(s2)+1)] for y in range(len(s1)+1)]
    dp = [[None for x in range(len(s2)+1)] for y in range(len(s1)+1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                c[i+1][j+1] = c[i][j]+1
                dp[i+1][j+1] = 'ok'
            elif c[i][j+1] > c[i+1][j]:
                c[i+1][j+1] = c[i][j+1]
                dp[i+1][j+1] = 'up'
            else:
                c[i+1][j+1] = c[i+1][j]
                dp[i+1][j+1] = 'left'
    p1 = len(s1)
    p2 = len(s2) 
    print(np.array(dp))
    s = []
    while c[p1][p2]:
        X =dp[p1][p2]
        if X =='ok':
            s.append(s2[p2-1])
            p1=p1-1
            p2=p2-1
        if X =='left':
            p2=p2-1
        if X =='up':
            p1=p1-1
    s.reverse()
    return "".join(s)


print(lcs('abdfg','abcdfg'))
