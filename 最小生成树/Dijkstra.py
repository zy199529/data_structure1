# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-06-08 21:37:22
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-06-09 09:16:09
import sys
max = sys.maxsize  # 设置无穷大
primgraph = graph = [[max, 12, max, max, max, 16, 14],
                     [12, max, 10, max, max, 7, max],
                     [max, 10, max, 3, 5, 6, max],
                     [max, max, 3, max, 4, max, max],
                     [max, max, 5, 4, max, 2, 8],
                     [16, 7, 6, max, 2, max, 9],
                     [14, max, max, max, 8, 9, max]]
chararray = ['0', '1', '2', '3', '4', '5', '6']
n = len(chararray)
charlist = []
charlist.append(chararray[0])
lowcost = []
lowcost.append(-1)
v = []
v = [0]*n
sum = 0
for i in range(1, n):
    lowcost.append(primgraph[0][i])
v[0] = 1
for _ in range(1, n):
    minid = 0
    min = max
    for j in range(1, n):
        if v[j] == 0 and lowcost[j] < min:
            min = lowcost[j]
            minid = j
    sum = sum+min
    if minid == 0:
        break
    charlist.append(chararray[minid])
    v[minid] = 1
    for j in range(1, n):
        if v[j] == 0 and lowcost[j] > (primgraph[minid][j]+lowcost[minid]):
            lowcost[j] = lowcost[minid]+primgraph[minid][j]
print(charlist)
