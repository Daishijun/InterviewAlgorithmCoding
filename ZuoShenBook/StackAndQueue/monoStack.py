# -*- coding: utf-8 -*-
# @Date    : 2019/6/5
# @Time    : 16:53
# @Author  : Daishijun
# @File    : monoStack.py
# Software : PyCharm

'''单调栈'''

#不包括重复元素
def momostack(arr):
    res = [[-1 for j in range(2)] for i in range(len(arr))]
    stack = []
    for i in range(len(arr)):
        while stack and arr[i] < arr[stack[-1]]:
            index = stack.pop()
            left = stack[-1] if stack else -1
            res[index][0] = left
            res[index][1] = i
        stack.append(i)
    while stack:
        index = stack.pop()
        left = stack[-1] if stack else -1
        res[index][0] = left
        res[index][1] = -1
    return res

if __name__ == '__main__':
    arr = [3,4,1,5,6,2,7]
    print(momostack(arr))


