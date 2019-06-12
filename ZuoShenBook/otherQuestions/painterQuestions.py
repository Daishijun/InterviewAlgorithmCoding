# -*- coding: utf-8 -*-
# @Date    : 2019/5/10
# @Time    : 17:27
# @Author  : Daishijun
# @File    : painterQuestions.py
# Software : PyCharm

'''
画匠问题 page555
'''

#动态规划， dp[i][j]==>i个画家搞定arr[0..j]所需要的最少时间
#没有使用空间压缩
def solution1(arr, num):
    '''
    :param arr:     各个任务所需时间
    :param num:     画家人数
    :return:    最小用时
    '''
    if not arr or len(arr) ==0 or num<1:
        raise Exception('err')
    sumArr =[0 for i in range(len(arr))]
    dp = [[0 for i in range(len(arr))] for j in range(num+1)]
    sumArr[0] = arr[0]    #任务所需时间的累加数组
    dp[1][0] = arr[0]
    for i in range(1,len(dp[0])):
        sumArr[i] = sumArr[i-1]+arr[i]
        dp[1][i] = sumArr[i]

    for i in range(2, num+1):
        for j in range(0, len(arr)):    #解决总共j幅画
            mintime = float('inf')
            for k in range(1, j):
                cur = max(dp[i-1][k], sumArr[j]-sumArr[k])
                mintime = min(mintime, cur)
            dp[i][j] = mintime
    return dp[num][len(arr)-1]

#空间压缩，只记录j个位置的画，所需要的最短时间，每次加一个画匠，更新list
def solution1_1(arr, num):
    if not arr or len(arr) == 0 or num<1:
        return 0
    dp = [0 for i in range(len(arr))]
    sumArr = [0 for i in range(len(arr))]
    sumArr[0] = arr[0]
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        sumArr[i] = sumArr[i-1] + arr[i]
        dp[i] = sumArr[i]    #只有1个画匠时
    for i in range(1, num):    #i==1时相当于两个画匠
        for j in range(len(arr)-1, i-1, -1):    #j最小能取到i，因为dp[]下标从0开始，i位置表示有i+1幅画，
            mintime = float('inf')              # 即，当有n个画匠的时候，只更新画数量大于等于n的记录，因为如果总的任务数量不变，人数增加，是无法更新最短用时的
            for k in range(i-1, j):             #保证前i-1个画匠每人最少负责一张画，不然会造成人员浪费，肯定不是最少用时
                cur = max(dp[k], sumArr[j] - sumArr[k])
                if cur<mintime:
                    mintime = cur
            dp[j] = mintime
    return dp[-1]



#四边形不等式 + 空间压缩
def solution2(arr, num):
    if not arr or len(arr) == 0 or num<1:
        return 0
    dp = [0 for i in range(len(arr))]
    sumArr = [0 for i in range(len(arr))]
    sumArr[0] = arr[0]
    dp[0] = arr[0]
    cands = [0 for i in range(len(arr))]
    for i in range(1, len(arr)):
        sumArr[i] = sumArr[i-1] + arr[i]
        dp[i] = sumArr[i]    #只有1个画匠时

    for i in range(1, num):    #i==1时相当于两个画匠
        for j in range(len(arr)-1, i-1, -1):    #j最小能取到i，因为dp[]下标从0开始，i位置表示有i+1幅画，
            minK = cands[j]
            maxK = cands[j+1] if j!=len(arr)-1 else j

            mintime = float('inf')              # 即，当有n个画匠的时候，只更新画数量大于等于n的记录，因为如果总的任务数量不变，人数增加，是无法更新最短用时的
            for k in range(minK, maxK+1):             #保证前i-1个画匠每人最少负责一张画，不然会造成人员浪费，肯定不是最少用时
                cur = max(dp[k], sumArr[j] - sumArr[k])
                if cur<mintime:
                    mintime = cur
                    cands[j] = k
            dp[j] = mintime
    return dp[-1]

if __name__ == '__main__':
    arr = [1,1,1,4,3]
    num = 3
    print(solution1(arr, num))
    print(solution1_1(arr, num))
    print(solution2(arr, num))

