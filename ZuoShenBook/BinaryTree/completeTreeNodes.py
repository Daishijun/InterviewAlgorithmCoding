# -*- coding: utf-8 -*-
# @Date    : 2019/5/18
# @Time    : 14:48
# @Author  : Daishijun
# @File    : completeTreeNodes.py
# Software : PyCharm

'''统计完全二叉树的节点数'''
'''通过检查右子树的最左节点是否到达最深(因为完全二叉树，在一层满了之后从下一层的最左边开始添加新节点)，每一步判断快速地获得一个完全子树的节点个数'''

def mostLeft(node, level):
    if not node:
        return 0
    while node.left :
        node = node.left
        level +=1
    return level    #以node为头的完全二叉树的深度

def bs(node, level, height):
    if level == height:
        return 1
    if mostLeft(node.right, level+1)==height:    #右子树的最左节点到达最深，说明node的左子树是满的
        return (1<<(height-level)) + bs(node.left, level+1, height)
    else:    #右子树是满的
        return (1<<(height-level-1)+ bs(node.left, level+1, height))

def nodeNum(head):
    if not head:
        return 0
    return bs(head, 1, mostLeft(head, 1))

