# -*- coding: utf-8 -*-
# @Date    : 2019/6/1
# @Time    : 20:33
# @Author  : Daishijun
# @File    : prac11.py
# Software : PyCharm

w, b = list(map(int, input().split()))

def dfs(rw, rb, h, n , count):
    if rw<n and rb<n:
        if h[0] == n-1:
            count[0] +=1
            count[0] %=1000000007
        elif h[0]<n-1:
            count[0] =1
            h[0] = n-1
        return
    if rw>=n:
         dfs(rw-n, rb, h, n+1, count)
    if rb>=n:
         dfs(rw, rb-n, h, n + 1, count)

if __name__ == '__main__':
    h = [0]; count = [0]
    dfs(w,b,h,1,count)
    print(h[0], count[0])
