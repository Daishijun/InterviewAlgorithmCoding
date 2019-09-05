# -*- coding: utf-8 -*-
# @Date    : 2019/4/23
# @Time    : 16:18
# @Author  : Daishijun
# @File    : validbrackets.py
# Software : PyCharm
'''
括号字符串的有效性和最长有效子串长度
'''

def isValid(string):
    if not string:
        return False
    statues = 0
    for i in range(len(string)):
        if string[i] not in ['(',')']:
            return False
        if string[i] == '(':
            statues+=1
        elif string[i] == ')':
            statues -=1
            if statues<0:
                return False
    return statues==0


#动态规划
def maxLength(string):
    if not string or string == '':
        return 0
    dp = [0 for i in range(len(string))]
    pre = 0
    for i in range(len(string)):
        if string[i] == ')':
            pre = i - dp[i-1]-1
            if pre >=0 and string[pre] == '(':
                if pre>0:
                    dp[i] = dp[i-1]+2+dp[pre-1]    #pre前面还有字符
                else:
                    dp[i] = dp[i-1]+2
    return max(dp)

if __name__ == '__main__':
    string = '())()(())'
    print(isValid(string))
    print(maxLength(string))