# -*- coding: utf-8 -*-
# @Date    : 2019/5/26
# @Time    : 14:31
# @Author  : Daishijun
# @File    : RoundB19.py
# Software : PyCharm

def prefix(string):
    res = [0 for i in range(len(string) + 1)]
    charset = set(list(string))
    res[0] = {x: 0 for x in charset}
    for i in range(len(string)):
        res[i + 1] = res[i].copy()
        res[i + 1][string[i]] = res[i][string[i]] + 1
    return res

def process2(prefix, indexlist):
    count = 0
    for [left, right] in indexlist:
        if right == left:
            count +=1
        else:
            leftpre = prefix[left-1]
            rightpre = prefix[right]
            odds = 0
            for key, value in rightpre.items():
                if (value-leftpre[key]) & 1 :
                    odds +=1
            if odds<2:
                count +=1
    return count

def process(string, indexlist):
    count = 0
    for [left, right] in indexlist:
        # print('left:',type(left), left, '\tright:', right)
        if right == left:
            count +=1
        else:
            subs = string[left-1:right]
            # print('subs:',subs)
            odds = 0
            for s in set(list(subs)):
                if odds >1:
                    break
                if subs.count(s) &1 :
                    odds +=1
            if odds<2:
                count +=1
    return count

T = int(input())
results = []
for i in range(T):

    N, Q = list(map(int, input().split()))
    string = input()
    indexlist = []
    prefixcount = prefix(string)

    for j in range(Q):

        indexlist.append(list(map(int, input().split())))
    # results.append(process(string, indexlist))
    results.append(process2(prefixcount, indexlist))

for i in range(T):
    print('Case #{}: {}'.format(i+1, results[i]))



