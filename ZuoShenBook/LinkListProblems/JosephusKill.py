# -*- coding: utf-8 -*-
# @Date    : 2019/5/4
# @Time    : 17:45
# @Author  : Daishijun
# @File    : JosephusKill.py
# Software : PyCharm

'''
约瑟夫圆环问题
'''

class Node():
    def __init__(self):
        self.value = 0
        self.next = None

def getLive(length, m):
    if length == 1:
        return 1
    else:
        return getLive(length-1, m)

def josephusKill2(head, m):
    if not head or head.next ==head or m<1:
        return head
    cur = head.next
    length = 1
    while cur !=head:
        length +=1
        cur = cur.next
    targetId = getLive(length, m)
    tar = head
    for i in range(targetId-1):
        tar = tar.next
    return tar
