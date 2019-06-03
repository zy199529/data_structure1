#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-05-31 22:43:28
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-05-31 22:46:20


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return i, j
    return 0
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums,target))