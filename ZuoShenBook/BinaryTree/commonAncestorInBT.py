# -*- coding: utf-8 -*-
# @Date    : 2019/5/16
# @Time    : 20:07
# @Author  : Daishijun
# @File    : commonAncestorInBT.py
# Software : PyCharm

'''
在二叉树中找到两个节点的最近公共祖先
'''

'''后序遍历走完整个流程，找到最低公共祖先时逐层返回'''

class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def lowestAncestor(head, node1, node2):
    if not head or head==node1 or head==node2:    #对应书上的第一种情况
        return head
    #后序
    left = lowestAncestor(head.left, node1, node2)
    right = lowestAncestor(head.right, node1, node2)
    if left != None and right != None:
        return head    #找到了最低公共祖先
    if left != None:
        return left
    else:
        return right

#用hash表保存每个节点对应的父节点信息

class Record():
    def __init__(self, head):
        self.mapdict = {}
        if head:
            self.mapdict[head] = None
        self.setMapdict(head)

    def setMapdict(self, head):
        if not head:
            return
        if head.left:
            self.mapdict[head.left] = head
        if head.right:
            self.mapdict[head.right] = head
        self.setMapdict(head.left)
        self.setMapdict(head.right)

    def query(self, node1, node2):
        path = []
        while node1:
            path.append(node1)
            node1 = self.mapdict[node1]
        while node2 not in path:
            node2 = self.mapdict[node2]
        return node2

###直接建立起任意两个节点的最低公共祖先
class Record2():
    def __init__(self, head):
        self.mapdict = {}
        self.initMap(head)
        self.setMap(head)

    def initMap(self, head):
        if not head:
            return



if __name__ == '__main__':
    nodelist = [Node(i) for i in range(1,9)]
    nodelist[0].left = nodelist[1]
    nodelist[0].right =  nodelist[2]
    nodelist[1].left = nodelist[3]
    nodelist[1].right = nodelist[4]
    nodelist[2].left = nodelist[5]
    nodelist[2].right = nodelist[6]
    nodelist[6].left = nodelist[7]

    node1 = nodelist[5]     #value==6
    node2 = nodelist[7]     #value == 8
    head = nodelist[0]
    lowest = lowestAncestor(head, node1, node2)
    print(lowest.value)

    print('###hash表记录每个节点对应的父节点信息，\
    然后根据node1记录反向路径，检查node2的反向路径与node1路径的交点')
    record = Record(head)
    print(record.query(node1, node2).value)

