# -*- coding: utf-8 -*-
# @Date    : 2019/4/2
# @Time    : 0:02
# @Author  : Daishijun
# @File    : p1.py
# Software : PyCharm
class Solution:
    # import copy
    def InversePairs(self, data):
        # write code here
        if data == None:
            return 0
        # copydata = copy.deepcopy(data)
        copydata = []
        for d in data:
            copydata.append(d)

        print(len(copydata))
        def Core(data, cdata, start, end):
            if start == end:
                cdata[start] = data[start]
                return 0
            length = (end - start) >> 1
            left = Core(cdata, data, start, start + length)
            right = Core(cdata, data, start + length + 1, end)
            leftp = start + length
            rightp = end
            indexc = end
            count = 0
            while leftp >= start and rightp >= start + length + 1:
                if data[leftp] > data[rightp]:
                    cdata[indexc] = data[leftp]
                    indexc -= 1
                    leftp -= 1
                    count += rightp - start - length
                else:
                    cdata[indexc] = data[rightp]
                    indexc -= 1
                    rightp -= 1
            while leftp >= start:
                cdata[indexc] = data[leftp]
                indexc -= 1
                leftp -= 1
            while rightp >= start + length + 1:
                cdata[indexc] = data[rightp]
                indexc -= 1
                rightp -= 1

            print('data:', data,'\n','copy:',cdata)
            print('count:',count + left + right )
            return count + left + right

        recount = Core(data, copydata, 0, len(data) - 1)

        return recount % 1000000007

if __name__ == '__main__':
    # s = Solution()
    # ls = [7,5,6,4]
    # print(s.InversePairs(ls))
    #
    a = '1'
    b = '3'
    li = list(range(258))
    # print(li[a])
    print(ord(a))
    print(type(ord(a)))
    print(chr(49))
    print(type(chr(49)))