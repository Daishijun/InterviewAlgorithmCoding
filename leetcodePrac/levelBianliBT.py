# -*- coding: utf-8 -*-
# @Date    : 2019/6/14
# @Time    : 17:00
# @Author  : Daishijun
# @File    : levelBianliBT.py
# Software : PyCharm

'''Leetcode 102 二叉树的层次遍历'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) :
        if not root:
            return [[]]
        res = []
        queue = [root]
        while queue:
            length = len(queue)
            level = []
            for i in range(length):
                cur = queue.pop(0)
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level)
        return res

if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    import sklearn








