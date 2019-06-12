# -*- coding: utf-8 -*-
# @Date    : 2019/6/4
# @Time    : 17:10
# @Author  : Daishijun
# @File    : diameterInBTree.py
# Software : PyCharm

'''Leetcode 543 二叉树的直径'''
'''
树形DP
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class ReType:
    def __init__(self, height, dia):
        self.height = height
        self.maxdia = dia


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        def helper(node):
            if not node:
                return ReType(0 ,0)
            leftRe = helper(node.left)
            rightRe = helper(node.right)
            height = max(leftRe.height, rightRe.height) +1
            dia = max(leftRe.maxdia, rightRe.maxdia, leftRe.height+rightRe.height+1)
            return ReType(height, dia)
        res = helper(root)
        return res.maxdia