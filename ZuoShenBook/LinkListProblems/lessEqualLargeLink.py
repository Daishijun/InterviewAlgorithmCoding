# -*- coding: utf-8 -*-
# @Date    : 2019/6/5
# @Time    : 10:01
# @Author  : Daishijun
# @File    : lessEqualLargeLink.py
# Software : PyCharm

'''将单向链表按某值划分成左边小，中相等，右边大的形式'''

'''不在乎排序后各个部分的顺序, 思路是将链表节点装到list中，
然后按value来进行partition调整：双指针，首尾指针分别与index位置交换。
'''

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def partition(arr, pivot):
    small = 0
    big = len(arr)-1
    index = 0
    while index < big:
        if arr[index].val < pivot:
            arr[index], arr[small] = arr[small], arr[index]
            index +=1
            small +=1
        elif arr[index].val == pivot:
            index +=1
        else:
            arr[index], arr[big] = arr[big], arr[index]
            big -=1
def linkPartition(head, pivot):
    if not head:
        return head
    cur = head
    length = 0
    while cur:
        length +=1
        cur = cur.next
    arr = [0 for i in range(length)]
    cur = head
    for i in range(length):
        arr[i] = cur
        cur = cur.next
    partition(arr)
    for i in range(1, length):
        arr[i-1].next = arr[i]
    arr[-1].next = None
    return arr[0]

'''需要保证3个部分每部分的顺序与原顺序相同。 思路：拆分成3个小链表，small链表，equal链表，large链表。
然后将这3个链表再拼起来。
'''
def linkpartition2(head, pivot):
    shead = None
    stail = None
    ehead = None
    etail = None
    lhead = None
    ltail = None
    cur = head
    while cur:
        nextnode = cur.next
        cur.next = None
        if cur.val < pivot:
            if not shead:
                shead = cur
                stail = cur
            else:
                stail.next = cur
                stail = cur
        elif cur.val == pivot:
            if not ehead:
                ehead = cur
                etail = cur
            else:
                etail.next = cur
                etail = cur
        else:
            if not lhead:
                lhead = cur
                ltail = cur
            else:
                ltail.next = cur
                ltail = cur
        cur = nextnode
    #连接起来
    if stail:
        stail.next = ehead    #如果没有相等部分，ehead为空，不会影响。
        if etail == None:
            etail = stail   #为了下面和大于部分合并
    if etail:    #经过上面的合并，如果这里仍然是None，说明前两部分都没有
        etail.next = lhead
    #返回头结点的三种情况
    if shead:
        return shead
    else:
        if ehead:
            return ehead
        else:
            return lhead



