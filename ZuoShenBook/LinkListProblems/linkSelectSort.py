# -*- coding: utf-8 -*-
# @Date    : 2019/6/11
# @Time    : 18:56
# @Author  : Daishijun
# @File    : linkSelectSort.py
# Software : PyCharm

'''单链表的选择排序'''
'''
时间复杂度N²
'''
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def getSmallestPreNode(head):
    smallPre = None
    small = head
    pre = head
    cur = head.next
    while cur:
        if cur.val < small.val:
            small = cur
            smallPre = pre
        pre = cur
        cur = cur.next
    return smallPre

def selectionSort(head):
    sortedtail = None
    cur = head
    smallPre = None
    small = None
    while cur :
        small = cur
        smallPre = getSmallestPreNode(cur)
        if smallPre!=None:
            small = smallPre.next
            smallPre.next = small.next
        # cur = cur.next if cur == small else cur
        if sortedtail == None:
            head = small
        else:
            sortedtail.next = small
        sortedtail = small
        cur = cur.next if small == cur else cur