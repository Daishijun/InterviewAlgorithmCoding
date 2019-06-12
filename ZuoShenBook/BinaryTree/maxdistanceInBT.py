# -*- coding: utf-8 -*-
# @Date    : 2019/5/18
# @Time    : 10:31
# @Author  : Daishijun
# @File    : maxdistanceInBT.py
# Software : PyCharm

'''二叉树节点间的最大距离问题'''
'''首尾都算到距离里, 只给定一个头结点，然后计算整个树的节点间最大距离'''
'''树形DP'''
'''信息整合：左子树上的最大距离，右子树上的最大距离，左子树高度，右子树高度'''

class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class ReturnType():
    def __init__(self, maxDistance, height):
        self.maxDis = maxDistance
        self.height = height

def process(head):
    if not head:
        return ReturnType(0, 0)
    leftRecord = process(head.left)
    rightRecord = process(head.right)

    height = max(leftRecord.height, rightRecord.height) + 1
    maxDistance = max([leftRecord.maxDis, rightRecord.maxDis, leftRecord.height+rightRecord.height+1])
    return ReturnType(maxDistance, height)

def getMaxDis(head):
    return process(head).maxDis

if __name__ == '__main__':
    nodelist = [Node(i) for i in range(1, 9)]
    nodelist[0].left = nodelist[1]
    nodelist[0].right = nodelist[2]
    nodelist[1].left = nodelist[3]
    nodelist[1].right = nodelist[4]
    nodelist[2].left = nodelist[5]
    nodelist[2].right = nodelist[6]
    nodelist[6].left = nodelist[7]

    print(getMaxDis(nodelist[0]))