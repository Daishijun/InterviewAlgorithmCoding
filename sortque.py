# -*- coding: utf-8 -*-
# @Date    : 2019/4/3
# @Time    : 23:16
# @Author  : Daishijun
# @File    : sortque.py
# Software : PyCharm

def core(N, reqlist):
    queue = list(range(1,N+1))
    rsum = 0
    for [event, K] in reqlist:
        if event == 1:
            queue.pop(0)
        elif event == 2:
            queue.pop(queue.index(K))
        elif event == 3:
            rsum += queue.index(K)+1
    return rsum

if __name__ == '__main__':
    N = 5
    req = [[1,0]]
    print(core(N, req))
