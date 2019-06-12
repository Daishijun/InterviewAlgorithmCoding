# -*- coding: utf-8 -*-
# @Date    : 2019/6/10
# @Time    : 15:02
# @Author  : Daishijun
# @File    : binaryTreeToLinkList.py
# Software : PyCharm

'''Leetcode 114  二叉树展开为链表'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#有待思考，用先序遍历也可以调整，有迭代和递归两种写法.
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right != None:
            root = root.right
        root.right = tmp


