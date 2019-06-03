#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-05-28 11:05:36
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-05-28 13:13:20
# 快速排序


def QuickSort(k, start, end):
    if start < end:
        i, j = start, end
        base = k[i]
        while i < j:
            while (i < j) and k[j] >= base:
                j = j-1
            k[i] = k[j]
            while (i < j) and k[i] <= base:
                i = i+1
            k[j] = k[i]
        k[i] = base
        QuickSort(k, start, i-1)
        QuickSort(k, j+1, end)
    return k

if __name__ == '__main__':
    k = [49, 89, 45, 87, 28, 9]
    print(QuickSort(k, 0, len(k)-1))
