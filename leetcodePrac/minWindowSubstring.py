#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/19 20:36
# @Author   : Daishijun
# @Site     : 
# @File     : minWindowSubstring.py
# @Software : PyCharm

'''LeetCode 76 最小覆盖子串'''

'''这个题主要的难点在于怎么衡量目前的窗口内包含子串字符， 用个字典，统计子串中有多少种字符，
每个字符的频次'''

'''这个做法是错的！！修改了部分代码，现在记录位置的dictionary里面每个value是一个list，
超时，可能是因为每次都要从list里挑选max和min.'''
def minwindow(string, substr):
    if len(string)<len(substr):
        return ''
    submap={}
    subindmap = {}
    for s in substr:
        submap[s] = submap.get(s, 0) +1
        subindmap[s] = []
    reslen = float('inf')
    ind = -1

    flag = 0
    target = len(submap)
    for i in range(len(string)):
        if string[i] in submap.keys():
            subindmap[string[i]].append(i)
            if len(subindmap[string[i]]) == submap[string[i]]:
                flag +=1
            if len(subindmap[string[i]]) > submap[string[i]]:
                subindmap[string[i]].pop(0)


        if flag == target:
            print('index:',i,'check ok!!!!!!')
            curlen = max([y for x in subindmap.values() for y in x]) \
                     - min([y for x in subindmap.values() for y in x]) +1
            print('curlen:', curlen)
            if curlen < reslen:
                ind = i
                reslen = curlen
        print('{}--{} submap:'.format(i, string[i]))
        for kk ,vv in submap.items():
            print('{}==>{}'.format(kk, vv))
        print('{}--{}  subindmap:'.format(i, string[i]))
        for kkk , vvv in subindmap.items():
            print('{}===>{}'.format(kkk, vvv))
        print('index:',i,'ind:', ind, 'len::', reslen)
    print('ind:', ind, 'len::', reslen)
    if reslen == float('inf'):
        return ''
    return string[ind-reslen+1:ind+1]


'''Leetcode 官方解法
使用双指针划定窗口，向右扩。
'''
class Solution:
    def minWindow(self, string: str, substr: str) -> str:
        if not string or not substr or len(string)<len(substr):
            return ''
        left = 0
        right = 0
        subdict = {}
        for s in substr:
            subdict[s] = subdict.get(s, 0) + 1
        letternum = len(subdict)

        ans = (float('inf'), None ,None)
        flag = 0
        windowdict = {}
        while right < len(string):
            cur = string[right]
            print('right while cur:', cur)
            windowdict[cur] = windowdict.get(cur, 0)+1
            print(windowdict[cur]==subdict[cur])
            if cur in subdict.keys() and  windowdict[cur] == subdict[cur]:
                flag +=1
            print('flag:', flag==letternum)
            while left<= right and flag == letternum:
                cur = string[left]
                print('left while cur:', cur)
                curlen = right-left+1
                if curlen < ans[0]:
                    ans = (curlen, left, right)

                windowdict[cur] -=1
                if cur in subdict.keys() and windowdict[cur] < subdict[cur]:
                    flag -=1
                left +=1
            right +=1
        return '' if ans[0] == float('inf') else string[ans[1]:ans[2]+1]







if __name__ == '__main__':
    # string = "ADOBECODEBANC"
    string = "a"
    # T = "ABC"
    T = "a"
    # S = Solution()
    # print(S.minWindow(string, T))
    # print(minwindow(string, T))
    adi = {1:2,3:9}

