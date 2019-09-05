#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/4 11:52
# @Author   : Daishijun
# @Site     : 
# @File     : treenodes.py
# @Software : PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def calNodes(node):
            stack = [node]
            tmp = 0
            while stack:
                cur = stack.pop(-1)
                tmp+=1
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
            return tmp
        def getnode(root,x):
            stack = [root]
            while stack:
                cur = stack.pop()
                if cur.val == x:
                    return cur
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)

        xnode = getnode(root,x)
        xnodes = calNodes(xnode)
        xleftnodes = calNodes(xnode.left) if xnode.left else 0
        xrightnodes = calNodes(xnode.right) if xnode.right else 0

        return xnodes<=n//2 or xleftnodes>n//2 or xrightnodes>n//2