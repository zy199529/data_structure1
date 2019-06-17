#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-05-28 10:18:18
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-06-17 19:53:17
# 归并排序基本思路：每次递归分解，分解成left和right，最后合并
def merge(left,right):
    i = 0
    j = 0
    result = []
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            result.append(right[j])
            j = j+1
        else:
            result.append(left[i])
            i = i+1
    if i==len(left):
        for h in range(j,len(right)):
            result.append(right[h])
    if j==len(right):
        for h in range(i,len(left)):
            result.append(left[h])
    return result

		
		

def MergeSort(nums):
    if len(nums) <= 1:
        return nums
    base = int(len(nums)/2)
    left = MergeSort(nums[:base])
    right = MergeSort(nums[base:])
    nums_sort = merge(left,right)
    return nums_sort
if __name__=='__main__':
    nums = [3,4,1,7,2,9,10,8]
    print(MergeSort(nums))
