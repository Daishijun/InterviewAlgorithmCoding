# -*- coding: utf-8 -*-
# @Date    : 2019/5/15
# @Time    : 14:19
# @Author  : Daishijun
# @File    : traversing.py
# Software : PyCharm

'''
遍历
'''

class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

'''
后序遍历
'''

def posOrder2(head):
    print('pos-order:')
    if head:
        cur = head
        stack = [cur]
        # s_c = None
        lastp = head    #记录上一步打印的节点
        while stack:
            s_c = stack[-1]    #栈顶
            if s_c.left and lastp !=s_c.left and lastp!=s_c.right:
                stack.append(s_c.left)
            elif s_c.right and lastp != s_c.right:
                stack.append(s_c.right)
            else:
                print(s_c.value)
                stack.pop()
                lastp = s_c

def posOrder(head):
    if not head:
        return
    posOrder(head.left)
    posOrder(head.right)
    print(head.value)

if __name__ == '__main__':
    nodelist = [Node(i) for i in range(1,8)]
    nodelist[0].left = nodelist[1]
    nodelist[0].right = nodelist[2]
    nodelist[1].left = nodelist[3]
    nodelist[1].right = nodelist[4]
    nodelist[2].left = nodelist[5]
    nodelist[2].right = nodelist[6]
    posOrder2(nodelist[0])
    # posOrder(nodelist[0])
