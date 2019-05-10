# -*- coding: utf-8 -*-
# @Date    : 2019/4/16
# @Time    : 17:57
# @Author  : Daishijun
# @File    : hanoi.py
# Software : PyCharm

'''
原问题，打印移动轨迹
'''

def func(n, start, help, end):
    if n==1:
        print('move from '+ start+ ' to '+end)
    else:
        func(n-1, start, end, help)    #把n-1个盘子从start 移动到辅助柱子
        func(1, start, help, end)       #start只剩一个盘子，将其从start直接移动到end
        func(n-1, help, start, end)     #再把n-1个盘子从辅助柱子移动到end

def priHanoi(n):
    if n>0:
        func(n, 'left', 'mid', 'right')
'''原问题结束'''

'''进阶题'''
def process(arr, ind, start, mid, end):    #返回的是把start上 1--ind+1的圆盘移动到end上去，需要的步骤数.
    if ind == -1:    #第0个圆盘，不存在，返回0
        return 0
    if arr[ind] !=start and arr[ind] != end:
        return -1
    else:
        if arr[ind] == start:
            return process(arr, ind-1, start, end, mid)
        else:    #第ind+1号圆盘在end上
            rest = process(arr, ind-1, mid, start, end)
            if rest == -1:
                return -1
            return rest + (1<<ind)

def step1(arr):
    if not arr:
        return -1
    return process(arr, len(arr)-1, 1,2,3)

def step2(arr):    #改成非递归
    if not arr:
        return -1
    start = 1; mid = 2; end = 3
    ind = len(arr)-1
    res = 0
    while ind>=0:
        if arr[ind] !=start and arr[ind] != end:
            return -1
        if arr[ind] == start:    #如果第ind+1个圆盘在start上，接下来要把1号到ind号圆盘从start 转移到mid上；所以交换mid 和 end的位置
            mid, end = end, mid
        elif arr[ind] == end:    #如果第ind+1号圆盘已经在end上了，说明至少走了2**ind步，接下来的操作是将1号到ind号圆盘从mid位置转移到end位置；所以交换mid和start的位置
            start, mid = mid, start
            res +=1<<ind
        ind -=1
    return res



if __name__ == '__main__':
    priHanoi(2)
    arr = [3,3,2,1]
    print(step1(arr))
    print(step2(arr))