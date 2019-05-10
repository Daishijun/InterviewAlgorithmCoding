# -*- coding: utf-8 -*-
# @Date    : 2019/4/13
# @Time    : 18:15
# @Author  : Daishijun
# @File    : figure_BFS.py
# Software : PyCharm

# 图的广度优先遍历
# 1.利用队列实现
# 2.从源节点开始依次按照宽度进队列，然后弹出
# 3.每弹出一个节点，就把该节点所有没有进过队列的邻接点放入队列
# 4.直到队列变空
from queue import Queue
def bfs(node):
    if node is None:
        return
    queue = Queue()
    nodeSet = set()
    queue.put(node)
    nodeSet.add(node)
    while not queue.empty():
        cur = queue.get()               # 弹出元素
        print(cur.value)                # 打印元素值
        for next in cur.nexts:          # 遍历元素的邻接节点
            if next not in nodeSet:     # 若邻接节点没有入过队，加入队列并登记
                nodeSet.add(next)
                queue.put(next)

