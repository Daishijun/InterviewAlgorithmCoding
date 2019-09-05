#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/18 14:27
# @Author   : Daishijun
# @Site     : 
# @File     : unionKsortedLinkList.py
# @Software : PyCharm

'''合并K个排序链表'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
方法一：把所有的节点都放在一个list里，然后排序，然后重新成链

这个暴力方法反而是最快的。
'''


'''
方法二：假设有k个链表，那么建一个容量为k的小根堆，然后每次pop堆顶，就是目前最小的。
这个方法利用了各个链表内部已排序的信息
'''

'''
方法三：一次选两个链表进行合并，直到最后都合并成一个，比如链1先和链2合并，合并结果再和链3合并。。
'''

'''
方法四： 也是将不同的链表两两进行合并，并不是用一个链然后去和其他链合并，而是两两合并。
'''
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):    #这里的interval和下面的i+interval需要学习，而且这里的末尾边界也要根据interval每轮更改。
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next

