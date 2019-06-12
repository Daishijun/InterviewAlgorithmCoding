# -*- coding: utf-8 -*-
# @Date    : 2019/5/15
# @Time    : 14:54
# @Author  : Daishijun
# @File    : EdgeNode.py
# Software : PyCharm

'''
打印二叉树的边界节点
两个标准：标准一， 标准二
'''

class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def getHeight(head, l):    #树的高度，或者说是深度，
    if not head:
        return l    #返回参数L
    return max(getHeight(head.left, l+1), getHeight(head.right, l+1))

def getDeep(head):
    if not head:
        return 0
    lefth = getDeep(head.left)
    righth = getDeep(head.right)
    return lefth+1 if lefth>=righth else righth+1

def setEdgeMap(head, l, edgeMap):
    if not head:
        return
    edgeMap[l][0] = head if edgeMap[l][0] == 0 else edgeMap[l][0]
    edgeMap[l][1] = head
    setEdgeMap(head.left, l+1, edgeMap)
    setEdgeMap(head.right, l+1, edgeMap)

def printLeafNotInMap(head, l, edgeMap):
    if not head:
        return
    if head.left == None and head.right == None and head != edgeMap[l][0] and head!=edgeMap[l][1]:
        print(head.value)
    printLeafNotInMap(head.left, l+1, edgeMap)
    printLeafNotInMap(head.right, l+1, edgeMap)

def printEdge1(head):
    if not head:
        return
    height = getHeight(head,0)
    edgeMap = [[0 for i in range(2)] for j in range(height)]
    setEdgeMap(head, 0, edgeMap)

    for i in range(height):
        print(edgeMap[i][0].value)
    printLeafNotInMap(head, 0, edgeMap)
    for j in range(height-1, -1, -1):
        if edgeMap[j][1] != edgeMap[j][0]:
            print(edgeMap[j][1].value)


'''
标准二, 从根节点开始区分左右，不带转折，向左就一直向左，右边界就是一直向右
'''
def leftEdge(head):
    if not head:
        return []

    leftlist = [head]
    while head.left:
        head = head.left
        leftlist.append(head)
    return leftlist

def rightEdge(head):
    if not head:
        return []
    rightlist = [head]
    while head.right:
        rightlist.append(head.right)
        head = head.right
    return rightlist

def printLeafNode(head, leftlist, rlist):
    if not head:
        return
    if head.left == None and head.right == None and head not in leftlist and head not in rlist:
        print(head.value)
    printLeafNode(head.left, leftlist, rlist )
    printLeafNode(head.right, leftlist, rlist)

def printEdge2(head):
    if not head:
        return
    leftedge = leftEdge(head)
    rightedge = rightEdge(head)
    for le in leftedge:
        print(le.value)
    printLeafNode(head, leftedge, rightedge)
    for j in range(len(rightedge)-1, -1, -1):
        if rightedge[j] not in leftedge:
            print(rightedge[j].value)

'''
标准二，书上的要求应该是求个包络，可以边界可以带转折，只要在整体最外侧就算
'''

def prLeftEdge(head, printflag):
    #为了逆时针，先序
    if not head:
        return
    if printflag or (head.left==None and head.right == None):
        print(head.value)
    prLeftEdge(head.left, printflag)
    prLeftEdge(head.right, printflag and (True if head.left == None else False))

def prRightEdge(head, printflag):
    if not head:
        return
    prRightEdge(head.left, printflag and (True if head.right == None else False))
    prRightEdge(head.right, printflag)
    if printflag or (head.left == None and head.right == None):
        print(head.value)

def printEdge2_book(head):
    if not head:
        return
    print(head.value)
    if head.left and head.right :
        prLeftEdge(head.left, True)
        prRightEdge(head.right, True)
    else:
        printEdge2_book(head.left if head.right==None else head.right)

if __name__ == '__main__':
    nodelist = [Node(i) for i in range(1,8)]
    nodelist[0].left = nodelist[1]
    nodelist[0].right = nodelist[2]
    nodelist[1].left = nodelist[3]
    nodelist[1].right = nodelist[4]
    nodelist[2].left = nodelist[5]
    nodelist[2].right = nodelist[6]

    # print(getHeight(nodelist[0], 0))
    # print(getDeep(nodelist[0]))
    printEdge1(nodelist[0])
    # printEdge2(nodelist[0])
    printEdge2_book(nodelist[0])