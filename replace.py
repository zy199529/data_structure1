#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-06-05 20:21:05
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-06-05 21:06:35
# def replace(strs):
#     strs =list(strs)
#     strs1=[]
#     for i in range(len(strs)):
#         if strs[i] == " ":
#              strs1.append("%20")
#              continue
#         strs1.append(strs[i])
#     return strs1


def replace(strs, n):
    blanks_count = strs.count(" ")  # 计算空格数目
    str_len = len(strs)
    str_len_new = str_len+2*blanks_count
    p1 = str_len-1
    p2 = str_len_new-1
    if str_len_new > n:
        return 0
    strs=list(strs)
    strs = strs+["" for i in range(p2-p1)]
    print(strs)
    i=p2
    while i>-1:
        if strs[p1] == " ":
            i=i-2
            strs[i]='%'
            strs[i+1]='2'
            strs[i+2]='0'
        elif strs[p1] != " ":
            strs[i]=strs[p1]
        i=i-1
        p1=p1-1
    return strs


if __name__ == "__main__":
    strs = "We are happy"
    # strs1=replace(strs)
    # strs1="".join(strs1)
    n=100

    print("".join(replace(strs,n)))
