#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-06-07 21:07:16
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-06-07 23:04:21
# 使用prim算法进行最小生成树的计算
import sys
MAX = sys.maxsize  # 设置无穷大
primgraph = [[MAX, 10, MAX, MAX, MAX, 11, MAX, MAX, MAX],
             [10, MAX, 18, MAX, MAX, MAX, 16, MAX, 12],
             [MAX, 18, MAX, 22, MAX, MAX, MAX, MAX, 8],
             [MAX, MAX, 22, MAX, 20, MAX, MAX, 16, 21],
             [MAX, MAX, MAX, 20, MAX, 26, 7, 19, MAX],
             [11, MAX, MAX, MAX, 26, MAX, 17, MAX, MAX],
             [MAX, 16, MAX, MAX, 7, 17, MAX, 19, MAX],
             [MAX, MAX, MAX, 16, 19, MAX, 19, MAX, MAX],
             [MAX, 12, 8, 21, MAX, MAX, MAX, MAX, MAX]]
chararray = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
charlist = []  # 存放最小生成树的结点
charlist.append(chararray[0])  # 存放第一个初始结点
n = len(chararray)  # 总长度
lowcost = []
lowcost.append(-1)
for i in range(1, n):
    lowcost.append(primgraph[0][i])
sum = 0  # 存放结点总长度
for _ in range(1, n):
    min = MAX
    minid = 0
    for j in range(1, n):  # 寻找最小权重的结点
    	if lowcost[j]!=-1 and lowcost[j]<min:
    		min = lowcost[j]
    		minid = j
    charlist.append(chararray[minid]) #最小生成树加入一个节点
    sum =sum+min
    lowcost[minid] = -1
    for j in range(1,n):
    	if lowcost[j]!=-1 and lowcost[j]>primgraph[minid][j]:
    		lowcost[j]=primgraph[minid][j]
print(sum)
print(charlist)