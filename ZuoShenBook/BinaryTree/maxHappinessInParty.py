# -*- coding: utf-8 -*-
# @Date    : 2019/5/18
# @Time    : 10:45
# @Author  : Daishijun
# @File    : maxHappinessInParty.py
# Software : PyCharm

'''派对的最大快乐值'''

class Employee():
    def __init__(self, happy, subordinates):
        self.happy = happy
        self.sub = subordinates

class ReturnType():
    def __init__(self, yesHeadMax, noHeadMax):
        self.yesMax = yesHeadMax
        self.noMax = noHeadMax

def process(head):
    yesX = head.happy
    noX = 0
    if len(head.sub) == 0:
        return ReturnType(head.happy, 0)
    else:
        for subem in head.sub:
            subInfo = process(subem)
            yesX += subInfo.noMax
            noX += max(subInfo.yesMax, subInfo.noMax)
        return ReturnType(yesX, noX)

def getMaxHappy(boss):
    info = process(boss)
    return max(info.yesMax, info.noMax)

