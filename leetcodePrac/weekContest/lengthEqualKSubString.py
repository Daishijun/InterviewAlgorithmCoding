#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/29 22:40
# @Author   : Daishijun
# @Site     : 
# @File     : lengthEqualKSubString.py
# @Software : PyCharm

'''Leetcode 5022  长度为K的无重复字符子串'''

class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if len(S) < K:
            return 0
        res = 0
        mapdict = {}
        curlen = 0
        path = []
        for ind in range(len(S)):
            if S[ind] not in mapdict:
                mapdict[S[ind]] = ind
                curlen +=1
                path.append(ind)
                # print('path:',path)
                # print('map:',mapdict)
            else:

                # print('meet chongfu', path, 'curlen:', curlen)
                if ind - mapdict[S[ind]] < K:
                    res += max(0, curlen-K+1)
                else:
                    res += max(0, curlen-K+1-(ind - mapdict[S[ind]]-K))
                curlen = ind - mapdict[S[ind]]
                # if ind - mapdict[S[ind]] < K:
                for i in range(path[0], mapdict[S[ind]]+1):
                    mapdict.pop(S[path.pop(0)])
                    # print('path:', path)
                    # print('map:', mapdict)
                mapdict[S[ind]] = ind
                path.append(ind)
                path.sort()
        # print('last len:',curlen)
        res += max(0 , curlen-K+1)
        return res

#超哥流弊
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if len(S) < K:
            return 0
        left = -1
        arr = [-1] *256
        length = len(S)
        res = 0
        for i in range(length):
            left = max(arr[ord(S[i])], left)    #记录无重复字符串的开始位置的前一个位置，遇到重复的时候会更新成上一次重复字符出现位置，表示开始考虑在重复位置之后开始的串
            arr[ord(S[i])] = i
            if i-left>=K:
                res +=1
        return res


if __name__ == '__main__':
    # S = "havefunonleetcode"
    K = 5
    # S = "home"
    S = "gdggdbjchgadcfddfahbdebjbagaicgeahehjhdfghadbcbbfhgefcihbcbjjibjdhfhbdijehhiabad"

    solution = Solution()
    print(solution.numKLenSubstrNoRepeats(S, K))


