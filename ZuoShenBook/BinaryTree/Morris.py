# -*- coding: utf-8 -*-
# @Date    : 2019/5/15
# @Time    : 17:18
# @Author  : Daishijun
# @File    : Morris.py
# Software : PyCharm

'''
Morris遍历， 空间复杂度为O(1)
'''

class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def morris(head):
    if not head:
        return
    cur = head
    mostRight = None
    while cur:
        mostRight = cur.left
        if mostRight:
            while mostRight.right and mostRight!=cur:
                mostRight = mostRight.right
            if mostRight.right == None:
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                mostRight.right = None
        cur = cur.right


'''Morris 先序'''
def morrisPre(head):
    if not head:
        return
    cur = head
    mostRight = None
    while cur:
        mostRight = cur.left
        if mostRight:
            while mostRight.right and mostRight!=cur:
                mostRight = mostRight.right
            if mostRight.right == None:
                mostRight.right = cur
                print(cur.value)    #打印
                cur = cur.left
                continue
            else:
                mostRight.right = None
        else:    #只能遍历到一次
            print(cur.value)
        cur = cur.right

'''Morris 中序'''

def morrisIn(head):
    if not head:
        return
    cur = head
    mostRight = None
    while cur:
        mostRight = cur.left
        if mostRight:
            while mostRight.right and mostRight!=cur:
                mostRight = mostRight.right
            if mostRight.right == None:
                mostRight.right = cur

                cur = cur.left
                continue
            else:
                print(cur.value)    #打印
                mostRight.right = None
        else:    #只能遍历到一次
            print(cur.value)
        cur = cur.right

'''Morris 后序'''
def reverseEdge(head):
    pre = None
    while head:
        next = head.right
        head.right = pre
        pre = head
        head = next
    return pre

def printReverEdge(head):
    tail  =  reverseEdge(head)
    cur = tail
    while cur:
        print(cur.value)
        cur = cur.right
    reverseEdge(tail)


def morrisPos(head):
    if not head:
        return
    cur = head
    mostRight = None
    while cur:
        mostRight = cur.left
        if mostRight:
            while mostRight.right and mostRight!=cur:
                mostRight = mostRight.right
            if mostRight.right == None:
                mostRight.right = cur
                printReverEdge(cur.left)   #打印
                cur = cur.left

            else:
                mostRight.right = None
                cur = cur.right
        else:
            cur = cur.right

    printReverEdge(head)
