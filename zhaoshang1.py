# -*- coding: utf-8 -*-
# @Date    : 2019/4/9
# @Time    : 19:54
# @Author  : Daishijun
# @File    : zhaoshang1.py
# Software : PyCharm

N = 100100
num = [0]*N
ans = [0]*N
def f(temp, cnt):
    temp = temp*2
    cnt +=1
    while temp < N :
        num[temp] +=1
        ans[temp] +=cnt
        cnt +=1
        temp *=2

if __name__ == '__main__':


    # n = int(input())
    # xlist = list(map(int, input().split()))
    n = 100000
    xlist = list(range(1,100001))

    for i in range(0, n):
        x = xlist[i]

        cnt = 0


        flag = True
        while x>0:
            num[x] +=1
            ans[x] +=cnt
            if flag:
                f(x, cnt)
            if x&1 :
                flag = True
            else:
                flag = False
            x = x>>1
            cnt +=1
    res = float('inf')
    for j in range(N):
        if num[j] == n:
            res = min(res, ans[j])
    print(res)
