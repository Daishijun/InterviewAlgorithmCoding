# -*- coding: utf-8 -*-
# @Date    : 2019/6/11
# @Time    : 11:39
# @Author  : Daishijun
# @File    : plusLinList.py
# Software : PyCharm

'''两个单链表生成相加链表'''

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


#使用额外存储空间，用两个栈，保存两个链表的内容。, 比链表逆序的方式快一点，可以省去第二次将链表逆序的时间
def addList1(head1, head2):
    stack1 = []
    stack2 = []
    while head1:
        stack1.append(head1.val)
        head1 = head1.next
    while head2:
        stack2.append(head2.val)
        head2 = head2.next
    ca = 0
    pre = None
    while stack1 or stack2:
        n1 = 0 if len(stack1) == 0 else stack1.pop()
        n2 = 0 if len(stack2) == 0 else stack2.pop()
        cursum = n1+n2+ca

        node = Node(cursum%10)
        node.next = pre
        pre = node
        ca = cursum//10
    if ca == 1:
        node = Node(1)
        node.next = pre
    return node

#将链表逆序，节省栈的空间
def reverseLink(head):
    pre = None
    while head:
        nextNode = head.next
        head.next = pre
        pre = head
        head = nextNode
    return pre

def addList2(head1, head2):
    head1 = reverseLink(head1)
    head2 = reverseLink(head2)
    ca = 0
    node1 = head1
    node2 = head2
    pre = None
    while node1 or node2:
        n1 = 0 if node1 == None else node1.val
        n2 = 0 if node2 == None else node2.val
        cursum = n1+ n2 + ca
        node = Node(cursum%10)
        node.next = pre
        pre = node
        ca = cursum//10
        node1 = None if node1==None else node1.next
        node2 = None if node2==None else node2.next

    if ca == 1:
        node = Node(1)
        node.next = pre
    reverseLink(head1)
    reverseLink(head2)
    return node







