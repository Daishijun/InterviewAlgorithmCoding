# -*- coding: utf-8 -*-
# @Date    : 2019/5/18
# @Time    : 17:46
# @Author  : Daishijun
# @File    : findKtimesNumInArray.py
# Software : PyCharm

'''在其他数都出现K次的数组中找到只出现一次的数字'''

'''左神，将每个数字转成k进制的32位，然后将每个数字的每一位进行无进位相加'''

def getKSysNumFromNum(value, k):    #左神的代码相当于是以左侧为最低位
    res = [0 for i in range(32)]    #32位数组
    index = 0
    while value:
        res[index] = value%k
        value = value//k
        index +=1
    return res

def getNumFromKSysNum(bitlist, k):
    res = 0
    for i in range(len(bitlist)-1, -1, -1):
        res = res * k + bitlist[i]

    return res

def getKSysNumFromNum_self(value, k):    #自己写的，低位在右侧， 从低位开始填，因为进制结果是余数的逆序
    res = [0 for i in range(32)]    #32位数组
    index = 31
    while value:
        res[index] = value%k
        value = value//k
        index -=1
    return res

def getNumFromKSysNum_self(bitlist, k):    #低位在右侧，这里从高位开始乘以k再和位进制上的数字相加，相当于对应位置*k的幂次
    res = 0
    for i in range(32):
        res = res * k + bitlist[i]

    return res

def setExclusiveOr(bitlist, value, k):
    curlist = getKSysNumFromNum(value, k)
    for i in range(len(curlist)):
        bitlist[i] = (bitlist[i] + curlist[i])%k    #无进位相加    #python传参，值传递还是引用传递取决于参数类型，如果是不可变参数：值传递； 可变参数：引用传递


def onceNum(arr, k):
    bitlist = [0 for i in range(32)]
    for i in range(len(arr)):
        setExclusiveOr(bitlist, arr[i], k)
    res =  getNumFromKSysNum(bitlist,k)
    return res

if __name__ == '__main__':
    arr = [3,2,3,3,1,2,2]
    k = 3
    # print(getKSysNumFromNum_self(value, k))
    # bilist = getKSysNumFromNum_self(value, k)
    # print(getNumFromKSysNum_self(bilist, k))
    print(onceNum(arr,k))

    barry = [1,2,3,4,5]
    c = barry
    def arrchange(arr):
        for i in range(len(arr)):
            arr[i] -=1
    print(barry)
    arrchange()
    print(barry)


