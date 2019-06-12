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

if __name__ == '__main__':
    s = 'leetcode'
    wordlist = ['leet','code']
    print(wordcanSplit(s, wordlist))








