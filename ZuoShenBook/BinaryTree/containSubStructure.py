# -*- coding: utf-8 -*-
# @Date    : 2019/5/16
# @Time    : 16:08
# @Author  : Daishijun
# @File    : containSubStructure.py
# Software : PyCharm

'''
判断t1树是否包含t2树全部的拓扑结构
'''


class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def check(head1, head2):    #同步遍历Tree1 和Tree2的节点，看是否包含
    if not head2:
        return True
    if not head1 or head1.value!= head2.value:
        return False
    return check(head1.left, head1.right) and check(head1.right, head2.right)

def contains(head1, head2):
    if not head2:
        return True
    if not head1:
        return False
    return check(head1, head2) or contains(head1.left, head2) or contains(head1.right, head2)    #遍历Tree1每个节点，看是否有包含Tree2的，进入check

'''剑指offer写法'''
'''本质一样，不过左神的写法更加精炼'''
def DoesHave(root1, root2):
    if not root2:
        return True
    if not root1:
        return False
    if root1.value != root2.value:
        return False
    return DoesHave(root1.left, root2.left) and DoesHave(root2.left, root2.right)

def HaveSub(root1, root2):
    if not root2:
        return True
    if not root1:
        return False
    results = False
    if root1.value == root2.value:
        results = DoesHave(root1, root2)
    if not results:
        results = DoesHave(root1.left, root2.left) or DoesHave(root1.righ, root2.right)
    return  results