#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-05-28 10:18:18
# @Last Modified by:   Lenovo
# @Last Modified time: 2019-05-28 11:34:30
# 归并排序基本思路：每次递归分解，分解成left和right，最后合并


def merge(left, right):
    # 合并
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i+1
        else:
            result.append(right[j])
            j = j+1
    if i == len(left):
        for h in right[j:]:
            result.append(h)
    else:
        for y in left[i:]:
            result.append(y)
    return result


def MergeSort(k):
    if len(k) <= 1:
        return k
    num = int(len(k)/2)
    left = MergeSort(k[:num])
    right = MergeSort(k[num:])
    return merge(left, right)
if __name__ == '__main__':
    k = [2, 5, 1, 7, 9, 6]
    print(MergeSort(k))
