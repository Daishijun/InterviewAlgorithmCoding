# -*- coding: utf-8 -*-
# @Date    : 2019/5/15
# @Time    : 20:45
# @Author  : Daishijun
# @File    : maxStrucBSTinBT.py
# Software : PyCharm

'''
找到二叉树中符合搜索二叉树条件的最大拓扑结构
'''

class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def isBSTNode(head, node, value):
    if not head:
        return False
    if head == node:
        return True
    return isBSTNode(head.left if head.value>value else head.right)

def maxTopo(head, node):
    if not head and not node and isBSTNode(head, node, node.value):
        return maxTopo(head, node.left) + maxTopo(head, node.right)+1
    return 0    #如果不符合二叉搜索结构, 则不能加入新节点

def bstTopoSize1(head):
    if not head:
        return 0
    #先序遍历，以每个节点为二叉搜索结构头结点的最大size
    maxsize = maxTopo(head, head)
    maxsize = max(bstTopoSize1(head.left), maxsize)
    maxsize = max(bstTopoSize1(head.right), maxsize)
    return maxsize


'''方法二，拓扑贡献记录'''
class Record():
    def __init__(self, left, right):
        self.left = left
        self.right = right

def modifyMap(node, value, mapdict, leftflag):
    if not node or node not in mapdict.keys():
        return 0
    record = mapdict[node]    #记录左右子树贡献值
    if (leftflag and node.value > value) or ((not leftflag) and node.value < value):    #不符合要求，要将拓扑结构去除
        mapdict.pop(node)
        return record.left+record.right+1    #要去掉的节点数
    else:
        #如果目前这个节点是可行的，需要根据其后继节点来确定要删除的节点数
        minus = modifyMap(node.right if leftflag else node.right, value, mapdict, leftflag)
        if leftflag:
            record.right -= minus
        else:
            record.left -= minus
        mapdict[node] = record
        return minus    #向上层调用返回要去掉的节点数.    #如果一直都是符合条件的，那么去掉的贡献度为0

def posOrder(node, mapdict):    #返回的是以node为二叉搜索头的情况下，拓扑结构最大节点数
    if not node:
        return 0
    lsum = posOrder(node.left, mapdict)    #后序遍历，在处理node的时候,其左右子节点对于各自为头的贡献度已经得到了
    rsum = posOrder(node.right, mapdict)
    modifyMap(node.left, node.value, mapdict, True)    #考察node为头结点的左子树的右边界
    modifyMap(node.right, node.value, mapdict, False)

    leftRecord = mapdict[node.left]
    rightRecord = mapdict[node.right]

    #根据得到的已经modify之后的node左右孩子节点的贡献度信息，得到node的左右子树贡献度信息
    leftscore = leftRecord.left + leftRecord.right +1 if leftRecord!=None else 0
    rightscore = rightRecord.left + rightRecord.right+1 if rightRecord!=None else 0
    mapdict[node] = Record(leftscore, rightscore)
    return max([leftscore+rightscore+1, lsum, rsum])    #三种情况：node自己为头，最大的拓扑结构数 来自 自己为头，左子树， 右子树。

def bstTopoSize2(head):
    mapdict = {}
    return posOrder(head, mapdict)