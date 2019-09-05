# -*- coding: utf-8 -*-
# @Date    : 2019/6/9
# @Time    : 14:10
# @Author  : Daishijun
# @File    : zhengZePattern.py
# Software : PyCharm

'''Leetcode 10 正则表达式匹配'''


class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        if not s or not p:
            return False

        return self.matchcore(s,p,0,0)

    def matchcore(self, s, p, sind, pind):
        if sind == len(s) and pind == len(p):
            return True
        if sind < len(s) and pind == len(p):
            return False
        if pind+1<len(p) and p[pind+1] == '*':
            if (sind<len(s) and s[sind] == p[pind]) or (p[pind] == '.' and sind<len(s)):
                #3种可能，可能匹配一次，可能匹配多次，可能匹配0次
                # return self.matchcore(s, p, sind+1, pind+2) or \
                #     self.matchcore(s, p, sind+1, pind) or \
                #     self.matchcore(s, p, sind, pind+2)

                return self.matchcore(s, p, sind+1, pind) or \
                    self.matchcore(s, p, sind, pind+2)
            else:
                return self.matchcore(s, p, sind, pind+2)  #匹配了0次
        if (sind<len(s) and s[sind] == p[pind]) or (p[pind] == '.' and sind<len(s)):
            #2种可能，对应的字符相同，或者pattern是“.”，都是只匹配一次。
            return self.matchcore(s, p, sind+1, pind+1)
        return False


#官方DP，但是没太看懂
class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        #    dp[i][j]表示text[i:]和pattern[j:]是否能够匹配。
        dp[-1][-1] = True    #就是dp[len(text)][len(pattern)] ==》表示结尾的两个空串
        for i in range(len(text), -1, -1):    #初始是string为空串， 检查pattern的最后一个字符能否匹配。
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}    #对应字符相同或者是"."
                if j+1 < len(pattern) and pattern[j+1] == '*':    #有’*‘， 这里是可以去匹配string空串的
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]    #匹配0次，或者匹配多次
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]    #匹配1次

        return dp[0][0]

#评论dp .和官方dp的目标和初始值相反。！！！存疑，好像有问题。。。
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #if not s or not p:
            #return False
        s_len = len(s)
        p_len = len(p)
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        #print(dp)
        dp[0][0] = True
        for i in range(p_len):
            if p[i] == "*" and dp[0][i - 1]:    ##这里确实有问题，在i==0的时候会取到倒数第一列。
                dp[0][i + 1] = True    #string是空串
        #print(dp)
        for i in range(s_len):
            for j in range(p_len):
                if p[j] == s[i] or p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == "*":
                    if p[j - 1] != s[i]:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    if p[j-1] == s[i] or p[j-1] == ".":
                        dp[i+1][j+1] = (dp[i][j+1] or dp[i+1][j]   or  dp[i+1][j-1])
        #print(dp)
        return dp[-1][-1]


if __name__ =='__main__':
    s = 'aa'
    p = 'a*'
    S = Solution1()
    print(S.isMatch(s,p))
    print(S.isMatch(s,p))