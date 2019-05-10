# -*- coding: utf-8 -*-
# @Date    : 2019/4/11
# @Time    : 16:56
# @Author  : Daishijun
# @File    : jianzhi.py
# Software : PyCharm

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        #write code here
        if n<= 0:
            return 0
        fisrtnum = n//pow(10,len(str(n))-1)
        if len(str(n)) == 1:
            return 1
        numfirst = 0
        if fisrtnum >1:
            numfirst = pow(10, len(str(n))-1)
        else:
            numfirst = n%pow(10, len(str(n))-1)+1
        numother = fisrtnum * (len(str(n))-1)*pow(10, len(str(n))-2)
        numRe = self.NumberOf1Between1AndN_Solution(n%(pow(10,len(str(n))-1)))
        return numfirst + numother + numRe

if __name__ == '__main__':
    # ss = Solution()
    # print(ss.NumberOf1Between1AndN_Solution(13))

    adic = {'rnn_unit': 8, 'epochs': 35, 'trainScore': 284.4018134822214, 'testScore': 374.33211518038024,
     'fixed_trainScore': 202.98579083511893, 'fixed_testScore': 277.10511465925975}

    bdic = {'rnn_unit': 8, 'epochs': 35, 'trainScore': 284.4018134822214, 'testScore': 374.33211518038024,
            'fixed_trainScore': 202.98579083511893, 'fixed_testScore': 277.10511465925975}

    import pandas as pd
    df = pd.DataFrame([adic, bdic], columns=['rnn_unit', 'epochs', 'trainScore', 'fixed_trainScore','testScore' ,'fixed_testScore'])
    print(df)

