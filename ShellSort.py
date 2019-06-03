#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-05-28 09:32:12
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-05-28 10:18:13
# 希尔排序


def ShellSort(k, n):
    gap = round(n/2)  # 划分增量
    while gap > 0:#当增量大于0
        for i in range(gap, n):
            while(k[i-gap] > k[i] and i >= gap):
                k[i], k[i-gap] = k[i-gap], k[i]
                i = i-gap
        print(k  )
        gap = round(gap/2)  # 每次减小增量，直到增量=0
    return k
if __name__ == '__main__':
    k = [2, 5, 7, 0, 1, 4, 6, 8, 9]
    print(ShellSort(k, len(k)))
