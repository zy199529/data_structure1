#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-05-31 22:48:33
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-06-02 23:04:21


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        l1num = []
        l2num = []
        while l1:
            l1num.append(l1.val)
            l1 = l1.next
        while l2:
            l2num.append(l2.val)
            l2 = l2.next


if __name__ == '__main__':
    a = 1
    b = 2
    print("monkey","\n","-",b)
    c = str(a)+'-'+str(b)
    print(c)
