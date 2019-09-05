#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/1 11:21
# @Author   : Daishijun
# @Site     : 
# @File     : p3.py
# @Software : PyCharm
#
# class Solution:
#     def canMakePaliQueries(self, s: str, queries) :
#
#         def checkhuiwen(string, k):
#             jic = 0
#             ouc = 0
#             stringlist = list(string)
#
#
#             for l in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',\
#                       'q','r','s','t','u','v','w','x','y','z']:
#                 if stringlist.count(l)%2 ==1:
#                     jic +=1
#                 else:
#                     ouc +=1
#
#             if len(stringlist) %2 == 0:
#                 if jic//2<=k:
#                     return True
#                 else:
#                     return False
#             elif len(stringlist) %2 ==1:
#                 if (jic-1)//2 <=k:
#                     return True
#                 else:
#                     return False
#
#         reslist = []
#         for que in queries:
#             reslist.append(checkhuiwen(s[que[0]:que[1]+1], que[2]))
#         return reslist


class Solution:
    def canMakePaliQueries(self, s: str, queries) :


        dic = {s[0]:1}
        prelist = [{},dic.copy()]
        def process(string):
            for i in range(1,len(string)):
                dic[string[i]] = dic.get(string[i], 0)+1
                prelist.append(dic.copy())

        def checkhuiwen(prelist, left, right, k):

            jic = 0
            ouc = 0
            # print("type:", type(prelist[right]))
            # print('###', prelist[right])
            for key , value in prelist[right].items():
                if (value-prelist[left-1].get(key,0))%2 == 0:
                    ouc +=1
                else:
                    jic +=1

            if (right-left+1) %2 == 0:
                if jic//2<=k:
                    return True
                else:
                    return False
            elif (right-left+1) %2 ==1:
                if (jic-1)//2 <=k:
                    return True
                else:
                    return False

        reslist = []
        process(s)
        # print(len(prelist))
        # print(prelist)
        for que in queries:
            reslist.append(checkhuiwen(prelist,que[0]+1,que[1]+1, que[2]))
        return reslist


if __name__ =='__main__':
    s = "abcda"
    queries = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]

    S = Solution()
    print(S.canMakePaliQueries(s,queries))