# -*- coding: utf-8 -*-
# @Date    : 2019/6/3
# @Time    : 9:07
# @Author  : Daishijun
# @File    : houseRobber.py
# Software : PyCharm

'''Leetcode 337 打家劫舍III'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ReturnType:
    def __init__(self, lai, bulai):
        self.lai = lai
        self.bu = bulai

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        def lai(node):
            if not node:
                return 0
            left = 0
            right = 0
            if node.left:
                left = bulai(node.left)
            if node.right:
                right = bulai(node.right)
            return node.val + left+right

        def bulai(node):
            if not node:
                return 0
            left = 0
            right = 0
            if node.left:
                left = max(lai(node.left), bulai(node.left))
            if node.right:
                right = max(lai(node.right), bulai(node.right))
            return left+right

        return max(lai(root), bulai(root))

    def process(self, node):
        lai = node.val
        bu = 0
        if node.left:
            resT = self.process(node.left)
            lai += resT.bu
            bu += max(resT.lai, resT.bu)
        if node.right:
            resT = self.process(node.right)
            lai += resT.bu
            bu += max(resT.lai, resT.bu)
        return ReturnType(lai, bu)


    def rob(self, root):
        if not root:
            return 0
        restype = self.process(root)
        return max(restype.lai, restype.bu)


'''LeetCode213 打家劫舍II'''


class Solution:
    def rob(self, nums) -> int:
        dp1 = [0 for i in range(len(nums)-1)]
        dp2 = [0 for i in range(len(nums)-1)]
        dp1[0] = nums[0]; dp1[1] = max(nums[0], nums[1])
        dp2[0] = nums[1]; dp2[1] = max(nums[1], nums[2])
        for i in range(2,len(nums)-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        for j in range(2, len(nums)-1):
            dp2[j] = max(dp2[j-1], dp2[j-2]+ nums[j+1])
        return max(dp1[-1], dp2[-1])

'''最优解'''
class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_helper(nums, 0, len(nums) - 2),
                   self.rob_helper(nums, 1, len(nums) - 1))

    def rob_helper(self, nums, low, high):
        prevMax = currMax = 0
        for index in range(low, high + 1):
            temp = currMax
            currMax = max(prevMax + nums[index], currMax)
            prevMax = temp
        return currMax