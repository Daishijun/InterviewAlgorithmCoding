#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/7 10:44
# @Author   : Daishijun
# @Site     : 
# @File     :
# @Software : PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete ) :
        res = []
        def postorder(node):
            if not node:
                return False
            leftflag = postorder(node.left)
            rightflag = postorder(node.right)
            if leftflag:
                node.left = None
            if rightflag:
                node.right = None
            if node.val in to_delete:

                if node.left :
                    res.append(node.left)
                if node.right:
                    res.append(node.right)

                return True
            return False
        postorder(root)
        if root.val not in to_delete:
            res.append(root)
        return res

if __name__ == '__main__':
    maderoot = TreeNode(1)
    maderoot.left = TreeNode(2)
    maderoot.right = TreeNode(3)
    maderoot.left.left = TreeNode(4)
    maderoot.left.right = TreeNode(5)
    maderoot.right.left = TreeNode(6)
    maderoot.right.right = TreeNode(7)
    deletelist = [3,5]
    S = Solution()
    # print(S.delNodes(maderoot, deletelist))
    res = S.delNodes(maderoot, deletelist)
    for node in res:
        print(node.val)

