# -*- coding: utf-8 -*-
# @Date    : 2019/5/15
# @Time    : 9:55
# @Author  : Daishijun
# @File    : jumpGame.py
# Software : PyCharm
'''
跳跃游戏
最少跳多少步能到达arr最后的位置    page247
'''

def jump(arr):
    if not arr:
        return 0
    jumpnum = 0
    curR = 0
    nextR = 0
    for i in range(len(arr)):
        if curR<i:
            jumpnum +=1
            curR = nextR
        nextR = max(nextR, i+arr[i])  #每遍历到一个位置，就更新一下最远能到达的位置。
    return jumpnum

if __name__ == '__main__':
    arr = [3,2,3,1,1,4]
    print(jump(arr))
