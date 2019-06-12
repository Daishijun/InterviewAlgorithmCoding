# -*- coding: utf-8 -*-
# @Date    : 2019/6/12
# @Time    : 10:12
# @Author  : Daishijun
# @File    : reBuildBinaryTree.py
# Software : PyCharm

'''重建二叉树   Page 62'''
'''Leetcode 105 根据先序和中序遍历序列构建二叉树'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder or not inorder or len(preorder) <1 or len(inorder)<1:
            return None
        length = len(preorder)
        return self.buildCore(preorder, 0, length-1, inorder, 0,length-1)

    def buildCore(self, prelist, prestart, preend, inlist, instart, inend):
        rootval = prelist[prestart]
        root = TreeNode(rootval)
        if preend == prestart:
            if instart == inend and prelist[prestart] == inlist[instart]:
                return root
            else:
                raise Exception('invalid input')
        rootIn = instart
        while rootIn<inend and inlist[rootIn] !=rootval:
            rootIn +=1
        if rootIn == inend and inlist[rootIn] != rootval:
            raise  Exception('invalid')
        leftlength = rootIn - instart
        leftPreend = prestart + leftlength
        if leftlength>0:
            root.left = self.buildCore(prelist, prestart+1, leftPreend, \
                                       inlist, instart, rootIn-1)
        if leftlength< preend - prestart:
            root.right = self.buildCore(prelist, leftPreend+1, preend, inlist, rootIn+1, inend)
        return root