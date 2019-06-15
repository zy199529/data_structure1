#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-06-14 21:18:26
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-06-15 09:55:17


class Node(object):

    def __init__(self, element, rchild=None, lchild=None):
        self.element = element
        self.rchild = rchild
        self.lchild = lchild


class Tree(object):

    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        # 根节点为空，加入节点
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur_code = queue.pop(0)
                if cur_code.lchild is None:
                    cur_code.lchild = None
                else:
                    queue.append(cur_code.lchild)
                if cur_code.rchild is None:
                    cur_code.rchild = None
                else:
                    queue.append(cur_code.rchild)

    def width_circle(self,root):
        if self.root is None:
            print("")
        else:
            queue = []
            queue.append(self.root)
            cur_node = queue.pop(0)
            print(cur_node.element, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)


def two_Tree(pre, mid):
    if len(pre) == 0:
        return None
    if len(pre) == 1:
        return Node(pre[0])
    else:
        r = Node(pre[0])
        id = mid.index(r.element)  # 找到索引
        p = pre[1:1+id]
        m = mid[:id]
        r.lchild = two_Tree(p, m)
        pe = pre[1+id:]
        me = mid[id+1:]
        r.rchild = two_Tree(pe, me)
    return r

def PrintFromTopToBottom(root):
        ans=[]
        if root==None:
            return ans
        else:
            q=[root]
            while q:
                node=q.pop(0)
                print(node.element, end=" ")
                ans.append(node.element)
                if node.lchild:
                    q.append(node.lchild)
                if node.rchild:
                    q.append(node.rchild)
            return ans
if __name__ == "__main__":
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    mid = [4, 7, 2, 1, 5, 3, 8, 6]
    T = Tree()
    r1 = two_Tree(pre,mid)
    PrintFromTopToBottom(r1)
    #T.width_circle(r1)