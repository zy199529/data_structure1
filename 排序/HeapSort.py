#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zy19950209
# @Date:   2019-05-28 14:55:09
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-05-28 15:13:20
# 堆排序----基本思路---将无序序列构建成大根堆，将堆顶元素和末尾元素交换，找到最大元素


def max_heapify(k, start, end):
    root = start
    while True:
        child = 2*root+1
        if child > end:
            break
        if child+1 < end and k[child] < k[child+1]:
            child = child+1
        if k[root] < k[child]:
            k[root], k[child] = k[child], k[root]
            root = child
        else:
            break


def HeapSort(k):
    n = len(k)
    first = int(n/2-1)  # 最后一个非叶子节点
    for start in range(first, -1, -1):  # 建立大根堆
        max_heapify(k, start, n-1)
    for end in range(n-1, 0, -1):
        k[end], k[0] = k[0], k[end]
        max_heapify(k, 0, end-1)
    return k
if __name__ == '__main__':
    k = [-1,6, 5, 3, 1, 8, 7, 2, 4]
    print(HeapSort(k))
