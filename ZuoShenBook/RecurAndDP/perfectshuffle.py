# -*- coding: utf-8 -*-
# @Date    : 2019/4/23
# @Time    : 14:00
# @Author  : Daishijun
# @File    : perfectshuffle.py
# Software : PyCharm
'''
完美洗牌问题
'''

#数组下标从1开始而不是从0开始
def modifyIndex1(ind, length):
    if ind<=(length>>1) :
        return 2*ind
    else:
        return 2*(ind-(length>>1))-1

#一个重要的结论：如果数组长度length = 2*N, 满足2*N = 3^k-1；则出发点有k个，分别是3^(p-1)，1<=p<=k。

def reverse(arr, L, R):
    while L<R:
        arr[L], arr[R] = arr[R], arr[L]
        L +=1
        R -=1

def rotate(arr, L, M, R):
    reverse(arr, L, M)
    reverse(arr, M+1, R)
    reverse(arr, L, R)

def cycles(arr, start, length, k):
    '''
    :param arr:
    :param start:    从arr的start位置开始，向右length长度的一段做下标连续推。
    :param length:
    :param k:    k个出发点
    :return:
    '''
    i = 0    #第几个出发点：[0,k)
    trigger = 1    #对应第i个出发点的具体出发位置
    while i<k:
        preValue = arr[start+trigger-1]    #因为arr的下表是从0开始算的，而出发位置trigger是从1开始算的，所以这里需要减一，与arr的下标统一。    !!记录被怼出来的元素
        cur = modifyIndex1(trigger,length)    #因为这里返回的位置也是从1开始计算的,所以在后续从arr里取元素时，需要减一
        while cur!=trigger:
            # print('start+cur-1, start:{s}, cur:{c}'.format(s=start, c=cur))
            tmp = arr[start+cur-1]    #被怼出来的元素
            arr[start+cur-1] = preValue
            preValue = tmp
            cur = modifyIndex1(cur, length)

        arr[cur+start-1] = preValue    #怼回到初始位置。
        i +=1; trigger*=3

def shufflein(arr, L, R):
    '''
    在arr[L...R]上做完美洗牌
    :param arr:
    :param L:
    :param R:
    :return:
    '''
    #首先需要将arr[L,R]切成一块一块的，满足每块长度为3^k-1，这样才能用k个初始位置的下标连续推把每一段搞定。
    while R-L+1>0:    #一块儿的长度
        length = R-L+1
        base = 3    #k=1时，3^k ==3
        k =1
        while base*3<=(length-1):    #找到最大的k，满足3^k <=length-1
            base *=3
            k +=1
        #此时划分出来的一块的长度是base-1,
        half  = (base-1)>>1

        #arr[L..R]的中间位置
        mid = (L+R)>>1
        rotate(arr, L+half, mid, mid+half)    #旋转
        cycles(arr, L, base-1, k)
        #解决了前base-1的一块，剩下的继续处理
        L = L + base-1

def shuffle(arr):
    if arr is not None and len(arr) >0 and len(arr)&1 ==0:
        shufflein(arr,0, len(arr)-1)

if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    shuffle(arr)
    print(arr)
    # print(modifyIndex1(4, 6))
    # arr = [1,2,3,4,5,6,7,8]
    # cycles(arr, 0, 8, 2)
    # print(arr)
