# -*- coding: utf-8 -*-
# @Date    : 2019/6/11
# @Time    : 18:54
# @Author  : Daishijun
# @File    : sortLink.py
# Software : PyCharm

'''LeetCode 148 排序链表'''

'''
归并排序

这里归并的时候，是从小的头开始填的，这和逆序对数不一样。其实对于排序而言，都是一样的。
这道题转成list然后排序再串起来会更快。
'''
class Node:
    def __init__(self,data):
        self.val =  data
        self.next = None

def sortLinkList(head):
    if not head or not head.next:
        return head
    mid = findMiddle(head)
    right= sortLinkList(mid.next)
    mid.next = None
    left  = sortLinkList(head)

    return merge(left, right)


def findMiddle(head):
    fast = head.next
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def merge(headleft, headright):
    '''

    :param headleft:
    :param headright:
    :return: 返回排序后的链表头结点
    '''
    left = headleft
    right = headright
    resnode = Node(0)
    tmpnode = resnode
    while left and right :
        if left.val <= right.val:
            tmpnode.next = Node(left.val)
            tmpnode = tmpnode.next
            left = left.next
        else:
            tmpnode.next = Node(right.val)
            tmpnode = tmpnode.next
            right = right.next
    while left:
        tmpnode.next = Node(left.val)
        tmpnode = tmpnode.next
        left = left.next
    while right:
        tmpnode.next = Node(right.val)
        tmpnode = tmpnode.next
        right = right.next
    return resnode.next