#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-05-27 09:06:05
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-05-28 09:11:27
# 冒泡排序：基本思想----两两比较相邻的关键字，如果反序则交换，知道没有反序的记录为止
# 优化冒泡排序的原因：如果进行一趟但是没有进行数据交换，说明已经有序，break即可，故加入flag------这点面试常考
# 稳定算法


def BubbleSort(k, n):
    flag = 1
    for i in range(n):
        flag = 0
        for j in range(1, n):
            if k[j-1] > k[j]:
                temp = k[j]
                k[j] = k[j-1]
                k[j-1] = temp
                flag = 1
        if flag == 0:
            break
        print(k)
    return k
if __name__ == '__main__':
    k = [2, 1, 3, 4, 5, 6, 7, 8, 9]
    print("最后结果：", BubbleSort(k, len(k)))
