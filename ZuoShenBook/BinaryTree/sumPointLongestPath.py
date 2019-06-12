# -*- coding: utf-8 -*-
# @Date    : 2019/5/15
# @Time    : 17:53
# @Author  : Daishijun
# @File    : sumPointLongestPath.py
# Software : PyCharm

'''
在二叉树中找到累加和为指定值的最长路径长度
'''
class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def proOrder(head, k, preSum, level, maxLen, sumDict):
    if not head:
        return maxLen
    curSum = preSum + head.value
    if curSum not in sumDict.keys():
        sumDict[curSum] = level
    if curSum - k in sumDict.keys():
        maxLen = max(maxLen, level- sumDict[curSum-k])
    maxLen = proOrder(head.left, k, curSum, level+1, maxLen, sumDict)
    maxLen = proOrder(head.right, k, curSum, level+1, maxLen, sumDict)

    if sumDict[curSum] == level:    #即将返回该节点的父节点了，如果是因为加上了这个节点才有的curSum 的数值，需要将这条记录去除。
        sumDict.pop(curSum)
    return maxLen

def maxLen(head, k):
    sumDict = {}
    sumDict[0] = 0    #加入初始记录，表明当什么都没有时，即在第0层（根节点为第1层）时，累加和为0
    return proOrder(head, k, 0 , 1, 0, sumDict)