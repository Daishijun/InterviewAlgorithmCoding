# -*- coding: utf-8 -*-
# @Date    : 2019/6/3
# @Time    : 18:15
# @Author  : Daishijun
# @File    : wordSplit.py
# Software : PyCharm

'''Leetcode 139 单词拆分, DP '''
'''
字节跳动夏令营第二题
'''

def wlist2index(s, wordlist):
    dic = {}
    for word in wordlist:
        beg = 0;
        end = len(s)
        wordlen = len(word)
        while True:
            startpos = s.find(word, beg, end)
            if startpos == -1:
                break
            if startpos not in dic.keys():
                dic[startpos] = [startpos + wordlen]
            else:

                dic[startpos].append(startpos + wordlen)
            if len(set(list(word))) == 1:
                beg = startpos+1
            else:
                beg = startpos + wordlen
    return dic

def segmentUnion(string, dic):
    targetlength = len(string)
    if 0 not in dic.keys():
        return False
    posstack = [0]
    while posstack:
        cur = posstack.pop()
        if cur == targetlength:
            return True
        if cur in dic.keys():
            posstack = posstack + dic[cur]
    return False

'''以上做法不行，超时而且坑多'''


def wordcanSplit(string, wordlist):
    if not string or string == '':
        return True
    if not wordlist:
        return False
    maxlen = 0
    for word in wordlist:
        if len(word)>maxlen:
            maxlen = len(word)
    dp = [False for i in range(len(string))]    #dp[i]表示以i位置结尾的string子串，可以被拆分成要求格式
    for i in range(len(dp)):
        p = i
        while p>-1 and i-p <= maxlen:    #这里的等号不能忘了
            if (dp[p] and (string[p+1:i+1] in wordlist)) or (p == 0 and (string[p:i+1] in wordlist)):
                dp[i] = True
                break
            p -=1    #p从结尾向前移动，表示切分出string[p:i+1]， 看能不能切出来。
    return dp[-1]


'''Leetcode 140 单词拆分II'''
'''回溯，core函数用于根据传入的子串开头位置来进行递归，返回的是从start位置往后到结尾的子串的划分结果list'''
class Solution:
    def wordBreak(self, string, wordDict):

        def word_breakcore(string, wordD, start):
            res = []
            if start == len(string):
                res.append('')
            for end in range(start+1, len(string)+1):
                if string[start: end] in wordD:
                    laterlist = word_breakcore(string, wordD, end)
                    for later in laterlist:
                        res.append(string[start:end]+('' if later=='' else ' ')+later)
            return res
        return word_breakcore(string, wordDict, 0)


'''回溯+记忆化搜索'''
class Solution:
    def wordBreak(self, string, wordDict):
        mapdict = {}    #key ==> start位置， value==>从start开始到结尾的串，能够拆分的字符串结果list
        def word_breakcore(string, wordD, start):
            if start in mapdict.keys():
                return mapdict[start]
            res = []
            if start == len(string):
                res.append('')
            for end in range(start+1, len(string)+1):
                if string[start:end] in wordD:
                    laterlist = word_breakcore(string, wordD, end)
                    for later in laterlist:
                        res.append(string[start:end]+('' if later=='' else ' ')+later)
            mapdict[start] = res
            return res
        return word_breakcore(string, wordDict, 0)


'''动态规划？？'''
'''
dp[]长度为n+1的数组，dp[k]用来存储s[0:k-1]可被拆分成的句子。
假如把s切分成两部分，s1,s2,希望s1是能够拆分并组成的句子，而s2也在WordDict中，这样就构成了一条s的拆分方法
根据s切分位置的不同，可能会存在多种结果，总的来说，s1部分由WordDict组成，s2在WordDict中，就可以了
对于dp[i]，相当于是在以s[i-1]为s2结尾字符的情况下去向前遍历寻找有效切分点j.
对于s1而言，相当于结尾字符为j-1，结果应该保存子dp[j]中。
对于满足要求的切分点，即s2在WordDict中，则获得dp[i]。
dp[i] = dp[j] + 1
'''
class Solution:
    def wordBreak(self, string, wordDict):

        dp = [[]]* (len(string)+1)    #dp[len(string)]==》s[0:len(string)-1]即整个字符串可以被拆分成的结果。
        #dp[i]的值是个list
        dp[0] = ['']
        for i in range(1, len(string)+1):
            relist = []
            for j in range(0, i):
                if len(dp[j])>0 and string[j:i] in wordDict:
                    for ahead in dp[j]:
                        relist.append(ahead + ('' if ahead=='' else ' ') + string[j:i])
            dp[i] = relist
        return dp[-1]




if __name__ == '__main__':
    s = 'leetcode'
    wordlist = ['leet','code']
    print(wordcanSplit(s, wordlist))
    'a'.isnumeric()









