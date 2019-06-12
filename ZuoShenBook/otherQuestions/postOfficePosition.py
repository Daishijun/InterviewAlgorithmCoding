# -*- coding: utf-8 -*-
# @Date    : 2019/5/11
# @Time    : 15:30
# @Author  : Daishijun
# @File    : postOfficePosition.py
# Software : PyCharm

'''
邮局选址问题    page 559
'''
def minDistance1(arr, num):
    '''

    :param arr:     坐标list
    :param num:     可修建的数量
    :return:
    '''

    if not arr or len(arr) == 0 or len(arr)<num or num<1:    #特殊情况：坐标位置< 要修建的邮局数量
        return 0

    w = [[0 for i in range(len(arr)+1)] for j in range(len(arr)+1)]
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):    #i<=j，而且如果是i==j，则表示只有一个城市，中心点就是自己，所以距离为0， 为初始值就行
            w[i][j] = w[i][j-1]+ arr[j] - arr[(i+j)>>1]

    print('w[][]:')
    for al in w:
        print(al)

    dp = [[0 for i in range(len(arr))] for j in range(num)]    #dp[a][b]   ==>表示在arr[0...b]上修建a+1个邮局，最少距离是多少。
    for j in range(0, len(arr)):
        dp[0][j] = w[0][j]    #只修建1个邮局时


    for i in range(1, num):
        for j in range(i+1, len(arr)):    #这里相当于也是把dp[][]赋值成上三角矩阵，，，因为这里要求的是dp的最后一个位置，所以没有问题。其实如果是i>=j，要修建的邮局数量比居民点还多，那么每个点修一个，距离为0，也是上三角矩阵。
            dp[i][j] = float('inf')
            for k in range(0, j+1):    #之前设置w[][]的维度，就是为了这里防止越界, 越界时为0
                dp[i][j] = min(dp[i][j], dp[i-1][k] + w[k+1][j])

    print('dp[][]:')
    for li in dp:
        print(li)
    return dp[num-1][len(arr)-1]


#四边形不等式
def minDistance2(arr, num):
    if not arr or len(arr) == 0 or len(arr) < num or num < 1:  # 特殊情况：坐标位置< 要修建的邮局数量
        return 0

    w = [[0 for i in range(len(arr) + 1)] for j in range(len(arr) + 1)]
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):  # i<=j，而且如果是i==j，则表示只有一个城市，中心点就是自己，所以距离为0， 为初始值就行
            w[i][j] = w[i][j - 1] + arr[j] - arr[(i + j) >> 1]
    dp = [[0 for i in range(len(arr))] for j in range(num)]  # dp[a][b]   ==>表示在arr[0...b]上修建a+1个邮局，最少距离是多少。
    cands = [[0 for i in range(len(arr))] for j in range(num)]  # 记录最后一段的最后划分，即最后一个邮局负责范围的起始点

    for j in range(len(arr)):
        dp[0][j] = w[0][j]
        cands[0][j] = 0    #只有一个邮局，自然是负责[0...len(arr)-1]

    minK = 0
    maxK = len(arr)-1    #最后一个邮局负责范围起始点的划分范围
    cur = 0
    for i in range(1, num):    #修建2个---num个邮局
        for j in range(len(arr)-1, i, -1):    #因为四边形不等式的原因，要取到上一行该位置和这一行右边的位置，所以只能从右向左更新
            dp[i][j] = float('inf')
            minK = cands[i-1][j]
            maxK = len(arr)-1 if j == len(arr)-1 else cands[i][j+1]
            for k in range(minK, maxK):
                cur = dp[i-1][k] + w[k+1][j]
                if cur <= dp[i][j]:
                    dp[i][j] = cur
                    cands[i][j] = k
    return dp[-1][-1]


if __name__ == '__main__':
    arr = [1,2,3,4,5,1000]
    num = 2
    print(minDistance1(arr, num))
    print(minDistance2(arr,num))


