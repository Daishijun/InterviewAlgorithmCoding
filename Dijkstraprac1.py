# -*- coding: utf-8 -*-
# @Date    : 2019/4/13
# @Time    : 17:58
# @Author  : Daishijun
# @File    : Dijkstraprac1.py
# Software : PyCharm


# edges表示邻接矩阵
edges = [[0, 1, 12, 666, 666, 666],
         [666, 0, 9, 3, 666, 666],
         [666, 666, 0, 666, 5, 666],
         [666, 666, 4, 0, 13, 15],
         [666, 666, 666, 666, 0, 4],
         [666, 666, 666, 666, 666, 0]]
dis = {2: 1, 3: 12, 4: 666, 5: 666, 6: 666}
visited = []

min_dis = None
min_dis_point = None

for i in range(len(dis)):
    sort_dis = sorted(dis.items(), key=lambda item: item[1])
    # 找到dis中距离起始点距离最小的点
    for p, d in sort_dis:
        if p not in visited:
            min_dis_point = p
            min_dis = d
            visited.append(p)
            break
    for j in range(len(edges)):
        # 权重小于666的为相邻点
        if edges[min_dis_point-1][j] < 666: #找相邻节点
            update = min_dis + edges[min_dis_point-1][j]    #从初始点经过min_dis_point到达j的距离
            # 若经过min_dis_point到j的距离比起点直达j的距离小，则更新
            if dis[j+1] > update:
                dis[j+1] = update

print(dis)

# 由于python中列表的索引是从0开始的，而我们的点是1-6，因此min_dis_point在邻接矩阵中的位置需要减一，
# 这里容易犯错，若是将点改为从0开始无论是写还是可读性都会好很多