# -*- coding: utf-8 -*-
# @Date    : 2018/8/28
# @Time    : 18:07
# @Author  : Daishijun
# @File    : prac01.py
# Software : PyCharm

import re
import sys

#
# num = int(sys.stdin.readline('num:'))
# stringlist = []
# for i in range(num):
#     stringlist.append((input('nums[{a}]'.format(a=i))))
#
# print('nums:',num)
# print('stringlist=',stringlist)

def fixedstr(strlist):

    for string in strlist:
        flag = 0
        strvec = []
        for s in string:
            print('strvec:', strvec)
            print('flag:',flag)
            if len(strvec)<2:
                strvec.append(s)
                continue
            if len(set(strvec)) ==1:
                flag = 1
            if s == strvec[-1]:
                if flag == 0:
                    flag =1
                    strvec.append(s)
                elif flag == 1:
                    continue
                elif flag == 2:
                    continue
            else:
                strvec.append(s)

                if flag ==1:
                    flag = 2

                elif flag ==2:
                    flag =0

        print(''.join(strvec))
'''剑指56'''
def Findfirst1(num):
    index = 0
    flag =1
    while index<32 and num &flag == 0:
        index +=1
        flag = flag<<1
    return index
def isBit1(num, index):
     num = num >>index
     return num&1

def FindNumsAppearOnce(datalist):
    if datalist == None or len(datalist)<2:
        return 0, 0
    orSum = 0
    for num in datalist:
        orSum = orSum ^ num
    firstindex = Findfirst1(orSum)

    res1 = 0
    res2 = 0
    for num in datalist:
        if isBit1(num, firstindex):
            res1 = res1 ^ num
        else:
            res2 = res2 ^ num
    return res1, res2

def FindNumAppearOnce2(datalist):
    if datalist == None:
        raise Exception('invalid input')
    bitlist = [0]*32
    for num in datalist:
        bitmark = 1
        for i in range(31,-1, -1):
            bit = num & bitmark
            if bit == 1:
                bitlist[i] +=1
            bitmark = bitmark<<1
    result =0
    for i in range(0,32,1):
        result = result<<1
        result += bitlist[i]%3
    return result


'''剑指57'''
def FindNumswithSum(datalist, s, reslist):
    '''
    题目一
    :param datalist:
    :param s:
    :param reslist:
    :return:
    '''
    smallindex = 0
    bigindex =len(datalist)-1
    found = False
    if datalist == None:
        return found
    while smallindex<bigindex:
        if datalist[smallindex] + datalist[bigindex] == s:
            found = True
            reslist[0] = datalist[smallindex]
            reslist[1] = datalist[bigindex]
            return found
        elif datalist[smallindex]+ datalist[bigindex] < s:
            smallindex+=1
        elif datalist[smallindex] + datalist[bigindex] >s:
            bigindex -=1

    return found

def PrintcontinueSeq(small, big):
    while small<=big:
        print(small, end='')
        small +=1
    print()
    return
def FindcontinuousSequence(s):
    '''
    题目二
    :param s:
    :return:
    '''
    if s <2:
        return
    small = 1
    big = 2
    middle = (s+1)>>1
    currentSum = small+big
    while small<middle:
        while currentSum>s and small<middle:
            currentSum -=small
            small+=1
        if currentSum == s:
            PrintcontinueSeq(small, big)
        big +=1
        currentSum+=big

'''剑指58'''
def Rverse(string):
    return string[::-1]
def ReverseSentence(sentence):
    if sentence == None:
        return
    sentence = Rverse(sentence)
    slist = sentence.split(' ')
    for i in range(len(slist)):
        slist[i] = Rverse(slist[i])
    return ' '.join(slist)


'''剑指59，队列最大值'''
def maxInWindows(nums,size):
    window = []
    maxlist = []
    if len(nums)< size or size<1:
        return
    for i in range(size):
        while len(window)>=1 and nums[i] > nums[window[-1]]:
            window.pop(-1)
        window.append(i)
    for i in range(size, len(nums)):
        maxlist.append(nums[window[0]])
        if len(window)>0 and window[0]<=i-size:   #注意这里的边界，比如当i=5时，5-3=2，此时窗内应该保留5，4,3号位置，所以2号位置及以前的要被移除
            window.pop(0)
        while len(window)>=1 and nums[i] > nums[window[-1]]:
            window.pop(-1)

        window.append(i)

    maxlist.append(nums[window[0]])
    return maxlist

#第二题，构造一个带有max功能的队列。
class InternalData:  #仅仅充当结构体
    def __init__(self, num, index):
        self.num = num
        self.index = index
class QueuewithMax:
    def __init__(self):
        self.data=[]
        self.maxindata=[]
        self.currentindex = 0



    def push_back(self, num):
        while len(self.maxindata)>0 and num>self.maxindata[-1].num:
            self.maxindata.pop(-1)
        internaldata = InternalData(num, self.currentindex)
        self.data.append(internaldata)
        self.maxindata.append(internaldata)
        self.currentindex +=1
    def pop_front(self):
        if len(self.data)<=0 or len(self.maxindata)<=0:
            raise Exception('queue is empty')
        if self.maxindata[0].index == self.data[0].index:
            self.maxindata.pop(0)
        self.data.pop(0)
    def max(self):
        if len(self.data)<=0 or len(self.maxindata)<=0:
            raise Exception('queue is empty')
        return self.maxindata[0].num

'''剑指60，骰子点数'''
gmaxValue=6
def PrintProbability(number):
    global gmaxValue
    if number<1:
        return
    maxSum = gmaxValue*number
    pProblist = [0]*(maxSum-number+1)
    Probability(number, pProblist)
    totle = pow(gmaxValue, number)
    for num in range(number, maxSum+1):
        ratio = pProblist[num-number]/totle
        print('sum={}, prob:{}'.format(num, ratio))
    del pProblist
    return



def Probability(number, problist):
    global gmaxValue
    for i in range(1, gmaxValue+1):
        ProbabilityIn(number, number, i, problist)

def ProbabilityIn(original, current, ssum, pProblist):
    if current == 1:
        pProblist[ssum-original]+=1
    else:
        for i in range(1, gmaxValue+1):
            ProbabilityIn(original, current-1, ssum+i, pProblist)

#基于循环
def PrintProbability2(number):
    global gmaxValue
    if number<1:
        return
    pProbmatirx = [[0]*(gmaxValue*number+1), [0]*(gmaxValue*number+1)]
    flag =0
    for i in range(1, gmaxValue+1):
        pProbmatirx[flag][i] = 1 #第一个骰子
    for k in range(2, number+1):
        for i in range(k):
            pProbmatirx[1-flag][i] = 0
        for i in range(k, gmaxValue*k+1):
            # pProbmatirx[1-flag][i] = 0
            for j in range(1,gmaxValue+1):
                if j > i:
                    break
                pProbmatirx[1-flag][i] += pProbmatirx[flag][i-j]
        flag = 1-flag

    total = pow(gmaxValue, number)
    for i in range(number, gmaxValue*number+1):
        print(pProbmatirx[flag][i])
        ratio = pProbmatirx[flag][i]/total
        print('sum:{}; prob:{}'.format(i, ratio))
    del pProbmatirx

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:

            return False
        if len(sequence) == 1:

            return True

        def Core(sequence):
            print(sequence)
            rootval = sequence[-1]
            print('rootval:',rootval)
            leftlength = 0
            left = True
            right = True

            for i in range(0, len(sequence) - 1):
                if sequence[i] < rootval:
                    leftlength = i+1
                else:
                    break
            for i in range(leftlength, len(sequence) - 1):
                if sequence[i] < rootval:
                    return False
            if leftlength > 0:
                print('left:', sequence[:leftlength])
                left = Core(sequence[:leftlength])
                print('left label:',left)
            if leftlength < len(sequence) - 1:
                print('right:', sequence[leftlength:-1])
                right = Core(sequence[leftlength:-1])
                print('right label', right)

            return left and right

        return Core(sequence)

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        relist = []
        path = []
        csum = 0

        def pathCore(root, expectNumber, csum, path):
            csum += root.val
            path.append(root)

            if not root.left and not root.right:
                if csum == expectNumber:
                    relist.append(path)
                    return
                else:
                    return
            if csum >= expectNumber:
                return
            if root.left:
                pathCore(root.left, expectNumber, csum, path)
            if root.right:
                pathCore(root.right, expectNumber, csum, path)
            return

        pathCore(root, expectNumber, csum, path)
        return relist.sort()


class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        relist = []
        slist = list(ss)
        print('split',slist)

        def Core(ss, slist, pos):
            print('slist:',slist)
            if pos == len(slist) - 1:
                if ''.join(slist) not in relist:
                    relist.append(''.join(slist))

            for i in range(pos, len(slist)):
                print('change place:', i)
                slist[i], slist[pos] = slist[pos], slist[i]
                Core(ss, slist, pos + 1)
                slist[i], slist[pos] = slist[pos], slist[i]

        Core(ss, slist, 0)
        return relist

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if  index<1:
            return None
        if index<5:
            return [1,2,3,5][index-1]
        fact2 = 2
        fact3 = 3
        fact5 = 5
        uglist = [2,3,5]
        for i in range(5, index+1):
            curug = min(min(fact2*2,fact3*3), fact5*5)
            uglist.append(curug)
            while fact2*2<curug:
                fact2 *=2
            while fact3*3<curug:
                fact3*=3
            while fact5*5<curug:
                fact5*=5
        return uglist[-1]


def powerspent(matirx, m ,n):
    r1 = 0; c1 = 0
    r2 = m-1; c2 = n-1
    curp = 0
    remat = [[0]*n for i in range(m)]
    while (r1<= r2 and c1<=c2):
        for c in range(c1, c2+1):
            curp += matirx[r1][c]
            remat[r1][c] = curp

        for r in range(r1+1, r2+1):
            curp += matirx[r][c2]
            remat[r][c2] = curp
        if r1 < r2:
            for c in range(c2-1, c1-1, -1):
                curp += matirx[r2][c]
                remat[r2][c] = curp
        if c1<c2:
            for r in range(r2-1, r1,-1):
                curp += matirx[r][c1]
                remat[r][c1] = curp
        c1 +=1; r1 +=1
        c2 -=1; r2 -=1
    return remat


if __name__ == '__main__':
    s = "(9-(10-(10-0-(3+(8+(0+(8-(10-8-(7-(2+(5+(6+(10+(3+(8+(3-(9+(1+(10+(1-(1+(6-2+0+(10-(9-(3-(3-9-(1-(7+(4-(2+(2-(10+(3+(7-(1-(4+(1+(1-(10-(5-(9+(9-4-(5-(1+8-(2-(1+(1-10-(4-(1+(4-(7)-(3-(8)+(5+5-(5-(9-(8+(8-4-1+(0-(1+(1+(10-(7+(2-(5-(4-(6+(2+(1-(2-(9+8+(2+(9-(9-(7+(10+1+(5)))-(2-(8+3+(5-(7-(3+(9)+(10+(0+(8-(1-(9)-(0+10-(3+(9-(0-(5-(7-(4-4+1+(7)-(10+(5+(9-(3+(5+(6-(0-(7-(1-(4+(6+(4-2-(4+(9-(6+9-8+1+(5+(7-9+3)+(10-(10+(2+(0-(5-(2+(10-(4-5-(7-(4-(7+(4)+6+10+(2-(7+(2))+(1)+(5-(7)-(10-(5+(7-(6-(2+(1-4)+(10-(5)+(4+(10+(4+(0+(10+(8-(8+(6+5-(1-(6-(1-(2+(4+(9-(3+(1+(10+(4)+(0+(3-(2-(9-(2-(3-(4-(2+(7-(6-(5+(7+(5+(5-(4+(0-(7+(2-(7+(9)-(6-(10)+(7+(2-(9-(9)+(4+(1-(8+(2-0-(2+(2+10)-(7-9-(9+(8-(5-8-(5)+(6+(10-(3-(2-(2+(7-2+(9+(3+(9+(2-(8+(5-(4+(4-(1-(9+(0+(6-(4-(3+(5-(2-(4-(6+(0+(4+3)-(8-(6+(9+(1+(2)-(8-(1+1+(5+(4-(3-(1-(7-4+(6+(9+(1+(4)+(6+(4+(2+(7-(1+(4-(8+(6+(8-(9-(2)-3-(0-(0)+(5+(7-(8)+(8-(2+(1)+1+(3+(6-(10-(2-4-(2-(2)+(8)+(3-(1-(1)+(6+(1+(9+(9+(5)-(4+(9+(10)+(0-(3+(3+0)+(6)-(6+(6)+(4-(8-1-5-(6)-(0))-(3)+(3-(3-(8-(10-(0-(4+(7)+(6-4))+1-(2-(1-(0-(0+(1-(0)-0+(5+(10-(2-(9-(9-10)+(3+(5-(6-(6-9-(5+5))+(7+(0)-(2-(7+2+(7-(2+(7+(4-(10+(4+(10-(3-(0-2+(9+(4-4-(3-(2)+(8+(5)+(1+1-(7+(3+(10+5-(0+(10-(9+(8-(0-(0+(8-(1+(0)+(6+(5+(5+(9)))+(4-(1-(3+(7+(9+(8-(1-8-(8+(0+(1+(1-(1)+(7+(6-(7-(8+(10)+1+(0-(10)+(8+(7+(10+(6+(10+(6)-(2+(2+(10-(8)-(5)))+(9-(1)+(4)+(5)-(6-(9)-(1+(6-(9+(10)+2-(4+(9-(4+1)-(0-(9)-(3)+(0)+(10)))+9)+(6+4+(6))+(5-(9))-(9-(2-(6+(7))-(6-(3+(5+(5-(0)-(5+(6-(5+(9-(2+(9+(1+(0+2+(7)-(3-(5+(2)+(4)+(6+(7-(3-(4)+(10+(4))+(3))-(3-(2)-(2+(2+(10+(3)+(3+(5)-(3-(0+(1)+(6+(4-(4)-(7-(9-(9)+(1)+(4)+(7))-(9))))-(3-(1+5-7-(7))-(4+(3+(7-(9+(8)-(9+(8-(3)+(10-(1)+(5)-(2-(4)+(0-(10-(7-(10+(1)+(1)-(4)-(10)))+(7)+(4-4)+0+9-(6))-(6+(5)))))-(8-(6)-(10+(5-(8)-(10+(3+(0+(6-(9)-(1)))-(0)-(9+(0+(1+(8+2-(4-(9-(4+(3+4)-(10+(1-(5)+(10-(4-(6-(4-(2+(4)-(9)-(4))))-3))))+(9)+(9+(0-(1+(5-(5+(7)-6-(8-(3-(3+(1)-(9-(7-(6)))-(2+(1))-(1+(2+(10))))+(6)+(0+(9-(1)-(10)))+(10-(1-(1)))-(0+(0-(2-(4-(6+(1))+(0)+(5)-(5+(5)-(4+(6)-(5)+(1-(7))))+(8)-(7))-3))-(7+(7+(9+(0+(10)-(7-(0-(2)-(6))-(2+(10)))+(7)+(3))+(8-(8+(10)-(8)+(0+(6-(2)-(1))+(3+(10+(10-(4+(7-(2)-(9-(2+(8))))+(7)-(7+10+(9-(2)+(0))-(6+(1)))+(10)+(2)-(7)-(4)-(10+(3-(6))))+(8-(1))-(10)))+(5+(3-(0-(1-(2+(3-(6-(4)-(1)+(4+(7+(3)-(7)+(4-(9))+(0-(4)+(9+(3-(9)+(4-(10+(6+(4)))+(4))+(10+(0-3-(8+(0-(6))-(5))-(9))-(6))))+2))+6+(6)+(1-(6))-(7-(1))-(8)+(9-(8))+(4)))-(0+7-(1)))-(2))+(0)))+(4-(7))-(5)-(8)-4+(1-(3-(8+(2+0)+(7)))))))-(4-(2))+(9))))+(7)-(2-(10+(4)-(8+(7)+(5-(4)-(6+6))-(2+(6)-(2+(4-(2-(8-(4)-(7+(5)-(10-(7)))))-(10+(9+(8)-(10)+(3-(7+(4+(2+(5)-(10+7+(2-(10)-(10+(3))+(0-(10+(8+(4+(7-(2)+(3+9))))+(7-(6+(2)-(2)+7+(5+(7+(10+(5-(4)-2+(5)+(1))+(0))))-(9))-5-(8)-(9-(4)-(10))-(8-(5)-(10)-7)+(5))-(4)))))+6+3+(3+(6+(9)))-10+(6)+(0)))))+(7)))+(1-(5)+(3-(3+6))+(5)+(7)-(9-(1))+(4+(1))+(2)))-(3))-(10)+(1)))))))))+(3)+2+(8-(4)))-(1))+(6-(8-(0)-(8-(0))-(2-(4+2)))-(9+1)))-(8-(8+(1-8-(7))))+7-(5+(5+(6+(10)+(8)))))))-(4))))-(4)-(6)+(10)-(5)))+(0+(2+(4))-(4-(2)+(0-(10-(4))))))+3-(10)))-(9+(9-(8-(7)-4))))+(6))-(4-(9))))-(1))+(10))))-(0+(9+7-(1)))))-(7)-(4)))-(9))))-7))))+(9))+(10))-(8-(9)))+(8))-(6)-(4)-(8)))))))))))))-(7)))))+(2-(6)-(0))))-(0)-(5+(9)+(9))+(3-(9))))+(8))))))))-(0-(0))+(7-(2))))))))-(6))-(8+(9))-(9+(2))-(2)+(9))-(4))+(7)-(1)-(6))-(2-0)))))))-(0)))))-(8+(0-(5))))+(9)-(1-(0)-(3)))-(3)-(0)))+(4)+(6))))-(5)+(1-(5)))))+(10))))-(5)+(0))))))-(6)))))))+(1))))))))-(5)))))))))+(8))))))))))))))))))-(7)+(10)))))))))))))-(4))))))-(10)-(4))+(1)+(3))-(1))))+(9))))))))+(2-(7-(4-(3+(0))))-(10)))))+0))))+(10)))))+(4)))))))))))+(3)))))))-(5)))))+(3)))))))))))))-(7)-(5-(2+(9))-(0))+(4)))+(10)))))-(1)))-(0))+(1))-(8+(10))))))-(10)-(10+(9)+(2))))-(1)))-(2))))+(4+(5))))))+(8))))))))))))))))))))))-(7)))-(3)))))))+(1))))-(7)-(3)+(4))))))-(6)))))))-(9-(3)))))))))))+(8))))))))))+(6))))))))))))))))))))))))))))))))))+(5))+(7))))))))))))))))))))))))-(10))))))+9)))))))"
    print(eval(s))

    # mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # import math
    # m = 3; n = 4
    # print(powerspent(mat,m, n))
    #
    # num = 13
    # print(math.log((num+1)&(-(num+1)), 2)+1)
    # numlist =list(range(1,101))
    # relist = [0]*100
    # print(relist)
    # for div in range(1,51):
    #     for i in range(100):
    #         if numlist[i] % div ==0:
    #             relist[i] +=1
    # print(relist)
    # cout = 0
    # for l in relist:
    #     if l&1 :
    #         cout +=1
    # print(cout)



    # for i in  range(0,100):
    #     for i in range()
    # #




    # import heapq
    # heap = []
    # l = [1,9,2,4,7,6,3]
    # k =3
    # for i in l:
    #     i = -i
    #     if len(heap)<k:
    #         heapq.heappush(heap, i)
    #     else:
    #         heapq.heappushpop(heap,i)
    # print([-h for h in heap])



    # num = int(input('num:'))
    # stringlist = []
    # for i in range(num):
    #     stringlist.append((input('nums[{a}]'.format(a=i))))
    #
    # print('stringlist=', stringlist)

    # stringlist =['aabbccddeeff','aabccdddfff ','aaabbcccee']
    # fixedstr(stringlist)
    # FindcontinuousSequence(15)

    # testlist = [1,2,4,7,11,15]
    # s = 15
    # relist = [0,0]
    # print(FindNumswithSum(testlist, s, reslist=relist))
    # print(relist)

    # testlist = [2,4,3,6,3,2,5,5,6,4]
    # re1 , re2 = FindNumsAppearOnce(testlist)
    # print(re1, re2)

    # testlist = [1,1,1,2,4,4,2,4,6,7,7,7,2]
    # res = FindNumAppearOnce2(testlist)
    # print(res)

    # teststring = 'what the fucking asshole.'
    # print(ReverseSentence(teststring))



    # df = pd.DataFrame(columns=[ 'testS'])
    # df['train'] = np.array([1,2,3,4,5,15,16])
    # df['predict'] = np.append(np.array([6,7,8,9,0,9]), np.array([0]*1))
    # print(df)
    # for i in range(10):
    #     df = df.append({'units':4,'epoch':20, 'trainS':i,'testS':i}, ignore_index=True)
    #     # df =df.append({'testS':i}, ignore_index=True)
    # print(df)
    # print([2,3,4,5][0])











