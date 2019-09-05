#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/18 10:55
# @Author   : Daishijun
# @Site     : 
# @File     :
# @Software : PyCharm

'''层次遍历'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        res, queue = [0,0], [root]
        level = 0
        while queue:
            level +=1
            level_len = len(queue)
            level_sum = 0
            while level_len>0:
                curnode = queue.pop(0)
                level_sum += curnode.val
                if curnode.left:
                    queue.append(curnode.left)
                if curnode.right:
                    queue.append(curnode.right)
                level_len -=1
            if res[0]<level_sum:
                res[0] = level_sum
                res[1] = level
        return res[1]