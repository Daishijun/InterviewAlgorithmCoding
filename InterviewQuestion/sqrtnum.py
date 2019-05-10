# -*- coding: utf-8 -*-
# @Date    : 2019/5/9
# @Time    : 15:10
# @Author  : Daishijun
# @File    : sqrtnum.py
# Software : PyCharm

'''
美团实习一面算法题：
1. 大数据中找到中位数
2. 大数据中找到topK
3. 实现sqrt方法
'''

'''
实现sqrt
'''
#二分法：
def sqrtNum(num):
    if num<0:    #注意过滤输入
        raise Exception('The input Num is Nagetive')
    delta = 1e-5   #允许的误差
    if num>=0 and num<=delta:
        return 0.0
    if abs(num-1.0)<=delta:
        return 1.0
    if num<1:    #注意【0...1】和【1...n】范围上，二分的初始位置是不一样的，因为当num<1的时候，num的平方会小于num
        left = num
        right = 1.0
    else:
        left = 1.0
        right = num
    mid = left
    while right-left>delta:
        mid = (left+right)/2     #注意点：：：不能用移位了，因为这里是float
        print('mid = ', mid)
        if mid*mid<num-delta:
            left = mid
        elif mid * mid > num + delta:
            right = mid
        else:
            return mid
    return mid


#牛顿法
def sqrtNewton(num):
    res = num
    lastres = num
    delta = 1e-5
    res = (res+num/res)/2
    while abs(res-lastres)>delta:
        lastres = res
        res = (res + num/res)/2
    return res




if __name__ == '__main__':
    num = 4
    print(sqrtNum(num))

    print(sqrtNewton(num))
