#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/3 17:07
# @Author   : Daishijun
# @Site     : 
# @File     : prac3.py
# @Software : PyCharm

'''二分图染色'''
n = int(input())
m = int(input())
book = [-1 for i in range(max(n,m)+1)]
arr = [[] for i in range(max(n,m)+1)]

def dfs(pre, now, cat):
    global flag
    book[now] = cat
    for i in range(len(arr[now])):
        if arr[now][i] != pre:
            if book[arr[now][i]]==-1:
                dfs(now, arr[now][i], 1-cat)
            elif book[arr[now][i]] == cat:
                flag = 1
                break

flag = 0
def main():


    for i in range(1, m+1):
        a, b = list(map(int, input().split()))
        arr[a].append(b)
        arr[b].append(a)
    print(arr)
    for i in range(1, m+1):
        if book[i] == -1:
            dfs(0, i, 1)
    if flag:
        print(0)
    else:
        print(1)
    return

main()

