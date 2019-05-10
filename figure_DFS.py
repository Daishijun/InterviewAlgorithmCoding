# -*- coding: utf-8 -*-
# @Date    : 2019/4/13
# @Time    : 18:15
# @Author  : Daishijun
# @File    : figure_DFS.py
# Software : PyCharm

# 图的深度优先遍历
# 1.利用栈实现
# 2.从源节点开始把节点按照深度放入栈，然后弹出
# 3.每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
# 4.直到栈变空
def dfs(node):
    if node is None:
        return
    nodeSet = set()
    stack = []
    print(node.value)
    nodeSet.add(node)
    stack.append(node)
    while len(stack) > 0:
        cur = stack.pop()               # 弹出最近入栈的节点
        for next in cur.nexts:         # 遍历该节点的邻接节点
            if next not in nodeSet:    # 如果邻接节点不重复
                stack.append(cur)       # 把节点压入
                stack.append(next)      # 把邻接节点压入
                set.add(next)           # 登记节点
                print(next.value)       # 打印节点值
                break                   # 退出，保持深度优先