# -*- coding: utf-8 -*-
# @Date    : 2019/5/18
# @Time    : 14:15
# @Author  : Daishijun
# @File    : differentBTNum.py
# Software : PyCharm

'''统计和生成所有不同的二叉树'''
'''输入仅为一个数N,表示中序遍历的结果是{1,2,3，...，N'''
'''求这种遍历结果可能的二叉树结构有多少种'''


'''动态规划，dp[i]表示i个节点的二叉树的可能数量'''
def numTrees(n):
    if n<2:
        return 1
    dp = [0 for i in range(n+1)]
    dp[0] = 1 #空树。
    for i in range(1, n+1):
        for j in range(1, i+1):    #第j个节点作为头的情况下，有多少种情况
            dp[i] += dp[j-1] * dp[i-j]
    return dp[n]


'''生成这些可能的二叉树结构，返回不同结构的头结点的list'''

class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def cloneTree(head):
    '''
    递归复制一颗树
    :param head:
    :return:
    '''
    if not head:
        return None
    res = Node(head.value)
    res.left = cloneTree(head.left)
    res.right = cloneTree(head.right)
    return res

def generate(start, end):
    '''
    :param start:
    :param end:
    :return:  返回所有可能结构的头结点
    '''
    res = []
    if start>end:
        res.append(None)
    for i in range(start, end+1):    #[start, end]来生成树结构
        head = Node(i)    #第i个节点为头
        leftsub =generate(start, i-1)
        rightsub = generate(i+1, end)
        for left in leftsub:
            for right in rightsub:
                head.left = left
                head.right = right
                res.append(cloneTree(head))
    return res




