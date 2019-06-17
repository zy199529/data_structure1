#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-05-28 08:52:20
# @Last Modified by:   Lenovo
# @Last Modified time: 2019-05-28 09:53:06
# 插入排序工作原理：对于每个未排序数据，在已排序序列中总后往前扫描，找到相应位置并插入。
# 直接插入排序被分为：有序数据和无序数据
# 每次从无序数据中选择一个数据插入到有序数据中


def InsertSort(k, n):
    for i in range(1, n):
        if k[i-1] > k[i]:
            temp = k[i]
            index = i
            for j in range(i-1, -1, -1):
                if k[j] > temp:
                    k[j+1] = k[j]
                    index = j
                else:
                    break
            k[index] = temp
    return k
if __name__ == '__main__':
    k = [1, 3, 2, 5, 7, 9, 0, 6, 4, 8]
    print(InsertSort(k, len(k)))
