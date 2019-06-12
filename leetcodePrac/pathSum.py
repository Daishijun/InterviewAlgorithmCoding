# -*- coding: utf-8 -*-
# @Date    : 2019/6/4
# @Time    : 11:14
# @Author  : Daishijun
# @File    : pathSum.py
# Software : PyCharm

'''Leetcode 437  路径总和III'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    count = 0
    def pathSum(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        outstack = [root]

        def preorder(proot, tar):
            if not proot:
                return 0
            if proot.val == tar:
                self.count +=1
            preorder(proot.left, tar-proot.val)
            preorder(proot.right, tar-proot.val)

        while outstack:
            curroot = outstack.pop()
            preorder(curroot, target)

            if curroot.left:
                outstack.append(curroot.left)
            if curroot.right:
                outstack.append(curroot.right)
        return self.count

'''最优解，借鉴左神书未排序数组中累加和为给定值的最长子数组系列问题， page 384'''
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        from collections import defaultdict
        if not root:
            return 0
        res  = 0
        dic = defaultdict(int)    #key：累加值， value:该累计值出现的次数
        dic[0] = 1    #一开始没有累加任何节点时，就已有0。
        def helper(node, cur):
            nonlocal res
            if node:
                cur += node.val
                res += dic[cur-target]
                dic[cur] +=1
                helper(node.left, cur)
                helper(node.right, cur)
                dic[cur] -=1   #去除这个点，把相应的累加值去掉
        helper(root, 0)
        return res





