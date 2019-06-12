# -*- coding: utf-8 -*-
# @Date    : 2019/5/16
# @Time    : 10:05
# @Author  : Daishijun
# @File    : levelPrintAndZigZagPrint.py
# Software : PyCharm

'''
二叉树的按层打印和zigzag打印
'''
class Node():
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

def leveltraver(head):    #用队列，根据每一层的节点个数，len(queue)来确定什么时候换行。
    if not head:
        return
    queue = [head]
    levellen = len(queue)
    levelnum = 1
    while queue :
        for i in range(levellen):
            if i == 0:
                print('Level {}:'.format(levelnum), end=' ')
            cur = queue.pop(0)
            print(cur.value, end=' ')
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        levellen = len(queue)
        levelnum +=1
        print()

def printByLevel(head):
    '''
    左神解决换行的思路是用两个变量来记录打印当前行的最右节点，和下一行的最右节点。当遍历到的（pop出来的cur）==当前行最右时，在将其左右孩子（不为空时）压入队列中之后，换行。
    :param head:
    :return:
    '''
    if not head:
        return
    last = head
    nextlast = None
    queue = [head]
    levelnum = 1
    print('level {}:'.format(levelnum), end=' ')
    while queue:
        cur = queue.pop(0)

        print(cur.value, end=' ')
        if cur.left:
            queue.append(cur.left)
            nextlast = queue[-1]
        if cur.right:
            queue.append(cur.right)
            nextlast = queue[-1]
        if cur == last and queue:
            levelnum +=1
            last = nextlast
            print()
            print('level {}:'.format(levelnum), end= ' ')


'''ZigZag'''
'''知识点：Java中，ArrayList是动态数组，当元素的个数到达一定规模时，会扩容，扩容的时间复杂度为O(N)，而且增加和删除元素的复杂度都比较高\
    但是LinkedList就是一个双端队列结构，即首尾都可以压入和弹出'''

def zigZagprint(head):
    if not head:
        return
    queue = [head]
    levellen = len(queue)
    levelNum = 1
    left2right = True
    while queue:
        for i in range(levellen):
            if i == 0:
                print('Level {num} {start} to {to}:'.format(start='left' if left2right else 'right', to='right' if left2right else 'left', \
                                                          num=levelNum), end=' ')
            if left2right:
                cur = queue.pop(0)
                print(cur.value, end=' ')
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            else:
                cur = queue.pop(-1)
                print(cur.value, end=' ')
                if cur.right:
                    queue.insert(0, cur.right)
                if cur.left:
                    queue.insert(0, cur.left)
        print()
        levellen = len(queue)
        levelNum +=1
        left2right = not left2right



if __name__ == '__main__':
    nodelist = [Node(i) for i in range(1,8)]
    nodelist[0].left = nodelist[1]
    nodelist[0].right = nodelist[2]
    nodelist[1].left = nodelist[3]
    nodelist[1].right = nodelist[4]
    nodelist[2].left = nodelist[5]
    nodelist[2].right = nodelist[6]

    leveltraver(nodelist[0])
    printByLevel(nodelist[0])
    print()
    zigZagprint(nodelist[0])

