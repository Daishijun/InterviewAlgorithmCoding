# -*- coding: utf-8 -*-
# @Date    : 2019/4/13
# @Time    : 17:58
# @Author  : Daishijun
# @File    : JingDong.py
# Software : PyCharm

modnum = 998244353

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.next = []
N = int(input())
edgelist = []
for i in range(N-1):
    edgelist.append(list(map(int, input().split())))


Nodelist = []
for i in range(1,N+1):
    Nodelist.append(TreeNode(i))
zinode = []
for [x,y] in edgelist:
    Nodelist[y-1].next.append(Nodelist[x-1])
    if y==1:
        zinode.append(Nodelist[x-1])
def preorder(root):
    if not root:
        return []
    stack = [root]
    result = 0
    while stack:
        cur = stack.pop()
        result+=1
        if cur.next:
            cur.next.reverse()
            stack += cur.next
    return result
print(max(preorder(node) for node in zinode))


