# -*- coding: utf-8 -*-
# @Date    : 2019/5/15
# @Time    : 20:19
# @Author  : Daishijun
# @File    : maxBSTinBT.py
# Software : PyCharm

'''
找到二叉树中的最大搜索二叉子树
'''

'''树形DP'''
class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class returnType():
    def __init__(self, maxBSTHead, maxBSTsize, minval, maxval):
        self.maxBSTHead = maxBSTHead
        self.maxBSTsize = maxBSTsize
        self.minval = minval
        self.maxval = maxval

def process(head):
    if not head:
        return returnType(None, 0, float('inf'), -float('inf'))
    leftData = process(head.left)
    rightData = process(head.right)
    minval = min([head.value, leftData.minval, rightData.minval])
    maxval = max([head.value, leftData.maxval, rightData.maxval])
    maxBSTHead  = leftData.maxBSTHead if leftData.maxBSTsize>=rightData.maxBSTsize else rightData.maxBSTHead
    maxBSTsize = max(leftData.maxBSTsize, rightData.maxBSTsize)
    if head.value > leftData.maxval and head.value < rightData.minval and leftData.maxBSTHead == head.left and rightData.maxBSTHead == head.right:
        maxBSTHead = head
        maxBSTsize = leftData.maxBSTsize + rightData.maxBSTsize + 1
    return returnType(maxBSTHead, maxBSTsize, minval, maxval)

def getMaxBST(head):
    return process(head).maxBSTHead
