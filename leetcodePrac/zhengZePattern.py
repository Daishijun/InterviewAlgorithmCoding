# -*- coding: utf-8 -*-
# @Date    : 2019/6/9
# @Time    : 14:10
# @Author  : Daishijun
# @File    : zhengZePattern.py
# Software : PyCharm

'''Leetcode 10 正则表达式匹配'''


class Solution:
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
                return self.matchcore(s, p, sind+1, pind+2) or \
                    self.matchcore(s, p, sind+1, pind) or \
                    self.matchcore(s, p, sind, pind+2)
            else:
                return self.matchcore(s, p, sind, pind+2)
        if (sind<len(s) and s[sind] == p[pind]) or (p[pind] == '.' and sind<len(s)):
            return self.matchcore(s, p, sind+1, pind+1)
        return False


#官方DP，但是没太看懂
class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]


if __name__ =='__main__':
    s = 'aa'
    p = 'a*'
    S = Solution()
    print(S.isMatch(s,p))
    print(S.isMatch(s,p))