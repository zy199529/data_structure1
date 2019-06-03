#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-05-30 14:42:04
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-05-30 15:57:47
# 二叉搜索树
# 插入


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None

# 插入搜索二叉树结点


def insert(root, val):
    if root is None:
        root = TreeNode(val)
    else:
        if val < root.val:
            root.lchild = insert(root.lchild, val)  # 递归的插入元素
        if val > root.val:
            root.rchild = insert(root.rchild, val)
    return root


def query(root, val):
    if root is None:
        return
    if root.val is val:
        return 1
    if root.val < val:
        return query(root.rchild, val)
    else:
        return query(root.rchild, val)


def findmin(root):
    if root.lchild:
        return findmin(root.lchild)
    else:
        return root


def delnum(root, val):  # 删除结点需要知道左孩子和右孩子是否为空
    if root is None:
        return
    if val < root.val:
        delnum(root.lchild, val)
    elif val > root.val:
        delnum(root.rchild, val)
    else:
        if (root.lchild and root.rchild):
            tmp = findmin(root.rchild)  # 找到后继结点
            root.val = tmp.val
            root.rchild = delnum(root.rchild, val)
        else:
            if root.lchild is None:
                root = root.lchild
            elif root.rchild is None:
                root = root.rchild
    return root

if __name__ == "__main__":
    root = TreeNode(3)
    root = insert(root, 2)
    root = insert(root, 1)
    root = insert(root, 4)
    print(query(root, 3))
    print(findmin(root))
    root = delnum(root, 1)

    print(query(root, 1))
