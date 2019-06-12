# -*- coding: utf-8 -*-
# @Date    : 2019/5/16
# @Time    : 14:10
# @Author  : Daishijun
# @File    : adjustBSTwrongPoints.py
# Software : PyCharm

'''
调整搜索二叉树中两个错误的节点
'''

class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def getTwoErrNodes(head):
    errlist = [None, None]
    if not head:
        return errlist
    stack = []
    pnode = head
    pre = None
    while pnode or stack:
        while pnode:
            stack.append(pnode)
            pnode = pnode.left
        cur = stack.pop()
        if pre !=None and pre.value>cur.value:
            errlist[0] = pre if errlist[0] == None else errlist[0]
            errlist[1] = cur
        pre = cur
        if cur.right:
            pnode = cur.right
    return errlist

def inOrder(head):
    if not head:
        return []
    return inOrder(head.left) + [head.value]+ inOrder(head.right)

def getTwoErrParents(head, e1, e2):
    parents = [None, None]
    if not head:
        return parents
    stack = []
    pnode = head
    while stack or pnode:
        while pnode:
            stack.append(pnode)
            pnode = pnode.left
        cur = stack.pop()
        if cur.left == e1 or cur.right == e1:
            parents[0] = cur
        if cur.left == e2 or cur.right == e2:
            parents[1] = cur
        if cur.right :
            pnode = cur.right
    return parents

###特殊情况特别多。
#区分的问题：
#（1）e1和e2有没有一个是头结点，如果有的话，谁是头结点
#（2）e1和e2是否相邻，如果相邻，谁是父节点
#（3）e1和e2分别是各自父节点的左孩子还是右孩子

def recoverBSTtree(head):
    errlist = getTwoErrNodes(head)
    parents = getTwoErrParents(head, errlist[0], errlist[1])

    print('###')
    print(errlist[0].value, errlist[1].value)


    e1 = errlist[0]
    e2 = errlist[1]
    e1P = parents[0]
    e2P = parents[1]
    e1Left = e1.left
    e1Right = e1.right
    e2Left = e2.left
    e2Right = e2.right

    if e1 == head:
        if e1 == e2P:
            e2.left = e1Left
            e2.right = e1
            e1.left = e2Left
            e1.right = e2Right
        elif e2 == e2P.left:
            e1.left = e2Left
            e1.right = e2Right
            e2P.left = e1
            e2.left = e1Left
            e2.right = e1Right
        else:
            e1.left = e2Left
            e1.right = e2Right
            e2P.right = e1
            e2.left = e1Left
            e2.right = e1Right
        head = e2    #!!!attention
    elif e2 == head:
        if e1 == e2Left:
            e1.left = e2
            e1.right = e2Right
            e2.left = e1Left
            e2.right = e1Right
        elif e1 == e1P.left:
            e1P.left = e2
            e1.left = e2Left
            e1.right = e2Right
            e2.left = e1Left
            e2.right = e1Right
        else:
            e1P.right = e2
            e1.left = e2Left
            e1.right = e2Right
            e2.left = e1Left
            e2.right = e1Right
        head = e1
    else:
        #e1和e2都不是头结点
        if e1 == e2P:    #相邻，e1是e2的头
            if e1P.left == e1:
                e1P.left = e2
                e1.left = e2Left
                e1.right = e2Right
                e2.left = e1Left
                e2.right = e1
            else:
                e1P.right = e2
                e1.left = e2Left
                e1.right = e2Right
                e2.left = e1Left
                e2.right = e1
        elif e2 == e1P:
            if e2P.left == e2:
                e2P.left = e1
                e1.left = e2
                e1.right = e2Right
                e2.left = e1Left
                e2.right = e1Right
            else:
                e2P.right = e1
                e1.left = e2
                e1.right = e2Right
                e2.left = e1Left
                e2.right = e1Right
        else:    #e1和e2不相邻
            if e1 == e1P.left:
                if e2 == e2P.left:
                    e1P.left = e2
                    e1.left = e2Left
                    e1.right = e2Right
                    e2P.left = e1
                    e2.left = e1Left
                    e2.right = e1Right
                else:
                    e1P.left = e2
                    e1.left = e2Left
                    e1.right = e2Right
                    e2P.right = e1
                    e2.left = e1Left
                    e2.right = e1Right
            else:
                if e2 == e2P.left:
                    e1P.right = e2
                    e1.left = e2Left
                    e1.right = e2Right
                    e2P.left = e1
                    e2.left = e1Left
                    e2.right = e1Right
                else:
                    e1P.right = e2
                    e1.left = e2Left
                    e1.right = e2Right
                    e2P.right = e1
                    e2.left = e1Left
                    e2.right = e1Right
    return head



if __name__ == '__main__':
    nodelist = [Node(i) for i in range(1,7)]
    nodelist[2].left = nodelist[1]
    nodelist[2].right = nodelist[4]
    nodelist[1].left = nodelist[0]
    nodelist[4].right = nodelist[5]
    nodelist[4].left = nodelist[3]
    print(inOrder(nodelist[2]))

    nodelist[2].value = 5
    nodelist[4].value = 3
    print(inOrder(nodelist[2]))


    # errs = getTwoErrNodes(nodelist[2])
    # print(errs[0].value, errs[1].value)
    # pars = getTwoErrParents(nodelist[2], errs[0], errs[1] )
    # print(pars)

    head = recoverBSTtree(nodelist[2])
    print('修正后:',inOrder(head))




