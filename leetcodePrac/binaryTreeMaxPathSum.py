#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/19 14:38
# @Author   : Daishijun
# @Site     : 
# @File     : binaryTreeMaxPathSum.py
# @Software : PyCharm

'''Leetcode 124'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ReturnType:
    def __init__(self, single, maxsum):
        self.single = single
        self.maxsum = maxsum
'''树形DP， 注意最大值和单边路径累加要和0对比，因为负值的时候可以不取之前的路径'''
class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        def process(head):

            if not head:
                return ReturnType(0,float('-inf'))
            left = process(head.left)
            right = process(head.right)
            single = max([left.single, right.single,0]) + head.val
            maxsum = max(left.maxsum, right.maxsum, head.val+max(0,left.single)+max(0,right.single))
            return ReturnType(single, maxsum)
        return process(root).maxsum



'''递归做法，和树形dp很像，设置全局变量记录最大值，返回的是从该结点开始的路径累加最大值，从左孩子经过
头结点然后到右节点的最大值用全局变量更新。'''
class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        def process(head):
            nonlocal maxres
            if not head:
                return 0
            left = max(process(head.left), 0)
            right = max(process(head.right), 0)

            sumNow = head.val + left + right

            maxres = max(maxres, sumNow)
            return head.val + max(left, right)

        maxres = float('-inf')
        process(root)
        return maxres
