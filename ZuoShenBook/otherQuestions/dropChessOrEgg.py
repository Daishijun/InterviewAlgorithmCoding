# -*- coding: utf-8 -*-
# @Date    : 2019/5/10
# @Time    : 11:29
# @Author  : Daishijun
# @File    : dropChessOrEgg.py
# Software : PyCharm

'''
丢棋子问题、丢鸡蛋问题。
N层大楼，找到不会摔碎的最高层数。

给定N层楼，给定K个棋子，求出最坏情况下扔棋子的最少尝试次数。
'''

#方法一，假设函数P(N, K)返回的是N层楼有K个棋子，在最坏情况下扔的最少次数
def Process1(nLevel, kChess):
    if nLevel == 0:
        return 0
    if kChess == 1:
        return nLevel
    minstep = float('inf')
    for i in range(1, nLevel+1):    #暴力从第1层开始遍历到当前所给定的最高层
        # if i == nLevel:
        #     pass
        minstep = min(minstep, max(Process1(i-1, kChess-1), Process1(nLevel-i, kChess)))
    return minstep+1

def solution1(nLevel, kChess):
    if nLevel<1 or kChess<1:
        return 0
    return Process1(nLevel, kChess)


#动态规划，因为P(N, K)的返回值只依赖于P(i-1, K-1)和 P(N-i, K)
def solution2(nLevel, kChess):
    if nLevel<1 or kChess<1:
        return 0
    if kChess == 1:
        return nLevel
    dp = [[0 for i in range(kChess+1)] for j in range(nLevel+1)]    #这里初始化为0矩阵，其中第一行dp[0][...]表示N==0时，不用尝试，所以dp[0][...] = 0, K = 0 时，
                                                                        # 自然也是0， 对应于第一个if;    这里是因为是可以取到第N层楼， 可以取到第K个棋子的。
    for i in range(1, len(dp)):
        dp[i][1] = i    #    对应于上面第二个if。
    for i in range(1, len(dp)):    #考虑总共有i层楼
        for j in range(2, len(dp[0])):    #考虑用j个棋子
            minstep = float('inf')
            for k in range(1, i+1):    #目前总共有i层楼时， 选择从第k层扔下去, 从第1层楼开始遍历到当前最高楼。
                minstep = min(minstep, max(dp[k-1][j-1], dp[i-k][j]))    #dp[i][j]依赖与第i行
            dp[i][j] = minstep +1
    return dp[nLevel][kChess]


def solution3(nLevel, kChess):
    if nLevel<1 or kChess<1:
        return 0
    if kChess == 1:
        return nLevel
    preArr = [ 0 for i in range(nLevel+1)]    #用了两个数组，来压缩空间。按照棋子数K来划分空间
    curArr = [ 0 for i in range(nLevel+1)]
    for i in range(1, len(curArr)):    #当K == 1时, 只有一个棋子
        curArr[i] = i
    for i in range(2, kChess+1):    #K == 2 都 K == kChess+1时
        tmp = preArr
        preArr = curArr
        curArr = tmp
        #交换了两个数组???
        for j in range(1, len(curArr)):
            minstep = float('inf')
            for k in range(1, j+1):    #是可以选择从j层扔下去的
                minstep = min(minstep, max(preArr[k-1], curArr[j-k]))    #相当于按照 K 来划分行。
            curArr[j] = minstep+1
    return curArr[nLevel]

def solution4(nLevel, kChess):    ###四边形不等式还是没理解
    if nLevel<1 or kChess<1:
        return 0
    if kChess == 1:
        return nLevel
    dp = [[0 for i in range(kChess + 1)] for j in range(nLevel + 1)]

    for i in range(1, len(dp)):
        dp[i][1] = i

    cands = [0 for i in range(kChess+1)]    #与dp的列数相同    , 表示在有index+1 个棋子时， 第一个棋子最优情况下 扔 在哪个位置
    for i in range(1, kChess+1):
        dp[1][i] = 1    #只有1层，只要有棋子，都只需要尝试1次。
        cands[i] = 1    #棋子仍在第1层

    for i in range(2, nlevel+1):
        for j in range(kChess, 1, -1):    #cands[]从右向左更新，更新了的表示解决i层楼问题， 未更新的表示解决i-1层楼问题
            minstep = float('inf')
            minEnum = cands[j]    #第一个棋子尝试的楼层下界。   此时的cands[j]的值是使用j个棋子解决i-1层楼获得最优解时候，第一颗棋子扔的位置
            maxEnum = i//2+1    #当前楼层总数的一半。
            if j != kChess:
                maxEnum = cands[j+1]    #使用j+1个棋子解决i层楼的最优解时候，第一个棋子扔下的楼层， 作为使用j个棋子解决i层楼问题的上界
            for  k in range(minEnum, maxEnum+1):
                cur  = max(dp[k-1][j-1], dp[i-k][j])
                if cur<= minstep:   #需要更新最小扔的次数了, 即此时选择的第一个棋子所扔的楼层才是最好的
                    minstep = cur
                    cands[j] = k
            dp[i][j] = minstep+1
    return dp[nLevel][kChess]


def log2N(num):    #要求num不能为负数
    res = -1
    while num!=0:
        res +=1
        num = num>>1
    return res

def solution5(nLevel, kChess):
    if nLevel<1 or kChess<1:
        return 0
    if kChess == 1:
        return nLevel

    bsTimes =  log2N(nLevel)+1
    if kChess >= bsTimes:
        return bsTimes    #如果棋子充足，就用二分法选定每个棋子扔的层数。，这里已经是最坏的情况：每次一扔就碎
    dp = [0 for i in range(kChess+1)]
    res = 0
    while 1:
        res +=1    #再扔一次
        previous = 0    #  前一次扔的时候，用 i-1个棋子能够搞定的最多层数
        for i in range(1, kChess+1):    #更新dp
            tmp = dp[i]    #前一次扔的时候能解决的最大楼层数
            dp[i] = dp[i]+ previous+ 1
            previous = tmp    #为i+1个棋子提供i个棋子能解决的层数
            if dp[i] >= nLevel:
                return res    #第一次超出了所给的楼层总数，输出此时扔的次数









if __name__ == '__main__':
    nlevel = 105
    k = 2
    # print(solution1(nlevel, k))
    print(solution2(nlevel, k))
    print(solution3(nlevel, k))
    print(solution4(nlevel, k))
    print(solution5(nlevel, k))
