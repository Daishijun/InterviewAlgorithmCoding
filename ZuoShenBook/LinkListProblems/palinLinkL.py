# -*- coding: utf-8 -*-
# @Date    : 2019/6/4
# @Time    : 17:41
# @Author  : Daishijun
# @File    : palinLinkL.py
# Software : PyCharm

'''判断链表是否为回文结构'''

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

'''方法二'''
def isPalin2(head):
    if not head or head.next == None:
        return True
    slow = head.next
    fast = head
    while fast.next and fast.next.next :
        slow = slow.next
        fast = fast.next.next
    stack = []
    while slow:
        stack.append(slow.val)
        slow = slow.next
    while stack:
        if stack.pop() != head.val:
            return False
        head = head.next
    return True

'''方法三,将后半部分链表逆序，然后从两头向中间判断，最后再逆序回来'''

def isPalin3(head):
    if not head or head.next == None:
        return True
    node1 = head
    node2 = head
    while node2.next and node2.next.next :
        node1 = node1.next
        node2 = node2.next.next
    node2 = node1.next
    node1.next = None

    while node2:
        node3 = node2.next
        node2.next = node1
        node1 = node2
        node2 = node3
    node3 = node1
    node2 = head
    res = True
    while node2 and node3:
        if node2.val != node3.val:
            res = False
            break
        node2 = node2.next
        node3 = node3.next
    #node1是末尾的节点
    node3 = node1.next
    node1.next = None
    while node3:
        node2 = node3.next
        node3.next = node1
        node1 = node3
        node3 = node2
    return res


