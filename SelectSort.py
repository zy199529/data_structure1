#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zy19950209
# @Date:   2019-05-27 10:01:01
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-05-27 10:31:16
# 选择排序基本思想：每一次从待排序的数据元素中选出最小的（或者最大的）一个元素，存放在序列的起始位置，知道全部的排序数据元素排完
# 选择排序不稳定
# 判断一个算法是否稳定---------排序前 2个相等的数，在序列的前后位置顺序和排序后两个前后位置顺序相同
# 相同-----稳定
# 不相同-----不稳定
# 排序算法----【3,3,1】  【1,3,3】 1,3互换位置不稳定
# 稳定排序的好处   对单一的数字无所谓啦，但是一群人按年龄排序，但是这些人还有身高体重，若不想破坏原先的身高体重次序，就必须使用稳定排序算法。


def SelectSort(k, n):
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if k[min] > k[j]:
                min = j
        if min != i:
            temp = k[min]
            k[min] = k[i]
            k[i] = temp
    return k
if __name__ == '__main__':
    k = [2, 1, 3, 4, 0, 9, 8, 6, 7, 5]
    print(SelectSort(k, len(k)))
