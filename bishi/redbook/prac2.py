#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/3 16:21
# @Author   : Daishijun
# @Site     : 
# @File     : prac2.py
# @Software : PyCharm

'''链表部分翻转'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

inputlist = list(map(int, input().split()))
K = int(input())
head = Node(inputlist[0])
tmp = head
for i in range(1,len(inputlist)):
    tmp.next = Node(inputlist[i])
    tmp = tmp.next

# checkhead = head
# while checkhead:
#     print(checkhead.val)
#     checkhead = checkhead.next
def resign(stack, left, right):
    cur = stack.pop(-1)
    if left:
        left.next = cur
    next = None
    while stack:
        next = stack.pop(-1)
        cur.next = next
        cur = next
    cur.next = right
    return cur

def reverseKNode(head, K):
    if K<2:
        return head
    stack = []
    newhead = head
    cur = head
    pre = None
    next = None
    while cur !=None :
        next = cur.next
        stack.append(cur)
        if len(stack) == K:
            pre = resign(stack, pre, next)
            newhead = cur if newhead == head  else newhead
        cur = next
    return newhead

reshead = reverseKNode(head, K)
res = []
while reshead:
    res.append(str(reshead.val))
    reshead = reshead.next
print(' '.join(res))