# -*- coding: utf-8 -*-
# @Date    : 2019/4/28
# @Time    : 19:13
# @Author  : Daishijun
# @File    : robotMoveTargetMethods.py
# Software : PyCharm

'''机器人达到指定方法数'''

def walk(N, cur, rest, P):
    '''

    :param N:   1--N个位置编号
    :param cur:     当前位置
    :param rest:     剩余步数
    :param P:     目标位置编号
    :return:
    '''
    if rest == 0:
        return 1 if cur == P else 0
    if cur == 0:
        return walk(N, 2, rest-1, P)
    if cur == N:
        return walk(N, N-1, rest-1, P)
    else:
        return walk(N, cur+1, rest-1, P)+ walk(N, cur-1, rest-1, P)

def ways1(N, M, K, P):
    '''

    :param N:
    :param M:     初始位置
    :param K:     总共移动步数
    :param P:     目标位置
    :return:
    '''
    if N<2 or K <1 or M<1 or M>N or P<1 or P>N:
        return 0
    else:
        return walk(N, M, K, P)

def walk2(N, M, K, P):
    if N<2 or K <1 or M<1 or M>N or P<1 or P>N:
        return 0
    dp = [[0 for i in range(N+1)] for j in range(K+1)]
    dp[0][P] = 1
    for i in range(1,K+1):
        for j in range(1, N+1):
            if j == 1:
                dp[i][j] = dp[i-1][2]
            elif j ==N:
                dp[i][j] = dp[i-1][N-1]
            else:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
    return dp[K][M]


if __name__ == '__main__':
    print(ways1(5,2,3,3))
    print(walk2(5,2,3,3))