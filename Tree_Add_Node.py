#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-05-30 13:18:57
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-05-30 14:34:02


# 初始化结点
class Node(object):

    def __init__(self, element, lchild=None, rchild=None):
        self.element = element
        self.lchild = lchild
        self.rchild = rchild

# 定义树


class Tree(object):
        # 定义根节点

    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        node = Node(item)
        # 假如根节点为空,加入根节点
        if self.root is None:
            self.root = node
            print(self.root)
            return
        # 若根节点存在
        else:
            queue = []
            # 新建队列
            queue.append(self.root)
            while queue:
                # 取出队头
                cur_node = queue.pop(0)
                # 左结点为空，放入左结点
                if cur_node.lchild is None:
                    cur_node.lchild = node
                    return
                # 左结点不为空，将左结点加入队列
                else:
                    queue.append(cur_node.lchild)
                # 右结点为空，放入右结点
                if cur_node.rchild is None:
                    cur_node.rchild = node
                    return
                # 右结点不为空，右结点加入队列
                else:
                    queue.append(cur_node.rchild)

    def width_circle(self):  # 层次遍历
        if self.root is None:
            print(" ")
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur_node = queue.pop(0)
                print(cur_node.element, end=' ')
                if cur_node.lchild is not None:
                    queue.append(cur_node.lchild)
                if cur_node.rchild is not None:
                    queue.append(cur_node.rchild)

    def preorder(self, node):
        if node is None:
            return
        else:
            print(node.element, end=' ')
            self.preorder(node.lchild)
            self.preorder(node.rchild)

    def inorder(self, node):
        if node is None:
            return
        else:
            self.inorder(node.lchild)
            print(node.element, end=' ')
            self.inorder(node.rchild)
    def postorder(self, node):
        if node is None:
            return
        else:
            self.postorder(node.lchild)
            self.postorder(node.rchild)
            print(node.element, end=' ')
            

if __name__ == "__main__":
    t = Tree()
    t.add(0)
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)
    t.width_circle()
    print('')
    t.preorder(t.root)
    print('')
    t.inorder(t.root)
    print('')
    t.postorder(t.root)
