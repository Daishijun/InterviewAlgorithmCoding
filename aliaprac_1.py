# -*- coding: utf-8 -*-
# @Date    : 2019/4/12
# @Time    : 19:54
# @Author  : Daishijun
# @File    : aliaprac_1.py
# Software : PyCharm

# plist = [0.3, 0.5, 0.7, 0.2, 0.9, 0.4]
# pplist = plist* (3//len(plist)) + plist[0:3%(len(plist))]
# print(pplist)
# print(len(pplist))
'''
N = int(input())
plist = []
for n in range(N):
    plist.append(float(input()))
pplist = plist* (100//len(plist)) + plist[0:100%(len(plist))]

pwinsum = 0
for i in range(0,3, 2):
    pwin = 1
    for j in range(i):
        pwin  *= (1-pplist[j])
    pwin *=pplist[i]
    pwinsum += pwin

print('%.4f'%pwinsum)
'''

M = 5; N = 5
K = 4
res = 0

if K<2:
    print(0)
elif K == 2:
    print(1)
else:

    for p in range(1, min(K, M+1)):
        countfish = 1
        if p ==2:
            countfish = M//2
        elif p>2:
            countfish = M-(p-1)-1
        for q in range(1, min(K-p+1, N+1)):
            print('p=', p, 'countfish:', countfish)
            countmeat = 1
            if q == 2:
                countmeat = N //2
            elif q >2:
                countmeat = N-(q-1)-1
            print('q=', q, 'meat:', countmeat)
            print('p=',p,'q=',q,'sum=',countfish*countmeat)
            res += countfish*countmeat

    print(res)