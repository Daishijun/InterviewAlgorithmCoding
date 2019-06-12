# -*- coding: utf-8 -*-
# @Date    : 2019/6/5
# @Time    : 9:25
# @Author  : Daishijun
# @File    : reversePartLink.py
# Software : PyCharm

'''反转部分单向链表'''

'''涉及修改链表的问题，需要注意头结点问题。这里就是需要考察反转部分是否需要考虑头结点。
'''

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def reversePart(head, start, end):
    linklen = 0
    node1 = head
    fPre = None
    tPos = None
    while node1:
        linklen +=1
        if linklen == start-1:
            fPre = node1
        if linklen == end+1:
            tPos = node1
        node1 = node1.next
    if start>end or start<1or end>linklen:
        return head
    node1 = head if not fPre else fPre.next
    node2 = node1.next
    node1.next = tPos
    while node2 != tPos:
        nodenext = node2.next
        node2.next = node1
        node1 = node2
        node2 = nodenext
    if fPre !=None:
        fPre.next = node1
        return head
    else:
        return node1