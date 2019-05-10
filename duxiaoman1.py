# -*- coding: utf-8 -*-
# @Date    : 2019/4/28
# @Time    : 21:36
# @Author  : Daishijun
# @File    : duxiaoman1.py
# Software : PyCharm

# n = int(input())
# lines = []
# for i in range(n):
#
#     line = list(map(int, input().split()))
#     lines.append([line[0], 1])
#     lines.append([line[1], 0])
#
# lines.sort()
# print(lines)
# t = 0
# res = 0
# for li in lines:
#     if li[1] == 1:
#         t +=1
#     else:
#         t-=1
#     res = max(res, t)
# print(res)

if __name__ == '__main__':
    li = [[2,0],[2,2],[2,1],[1,9],[1,0]]
    li.sort()
    print(li)