#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/11 11:29
# @Author   : Daishijun
# @Site     : 
# @File     : pra2.py
# @Software : PyCharm

'''2'''
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # def backtrack(ind, f, target):
        #     res = 0
        #     if ind == d-1:
        #         if target >=0 and target<=f:
        #             return 1
        #         else:
        #             return 0
        #     for i in range(1, min(f+1, target+1)):
        #         res +=backtrack(ind+1, f, target-i)
        #     return res
        # return backtrack(0, f, target)

        dp = [[0 for i in range(target + 1)] for j in range(d)]
        for i in range(d):
            dp[i][0] = 0

        for j in range(1,min(f+1, target+1)):
            dp[0][j] = 1
        for ind in range(1, d):
            for rest in range(1, target + 1):
                dp[ind][rest] = dp[ind][rest-1]+dp[ind-1][rest-1]
                if rest-f>=0:
                    dp[ind][rest] -= dp[ind-1][rest-f-1]
                # for k in range(1, f+1):
                #     if rest-k<0:
                #         break
                #     dp[ind][rest] += dp[ind-1][rest-k]



        print('dp:', dp)
        return dp[d - 1][target]

if __name__ == '__main__':
    # S = Solution()
    # print(S.numRollsToTarget(2, 6 , 7))
    # import numpy as np
    # from scipy.sparse import coo_matrix, csc_matrix, lil_matrix, csr_matrix
    # matoo = coo_matrix((10**9,10**9), dtype=np.int8)
    # mat = matoo.tocsr()
    # print(mat[0,2])
    #
    # mat[0,np.array([1,6,9])] = 1
    # mat[1,3] = 1
    # print(mat[1,3])

    # print(mat.todense())
    # mat[0,3] = 1
    # print(mat.todense())

    # temp = np.arange(3)*2
    # print(temp)
    # #
    # a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    # a[1][np.array([0,1])] +=1
    # print(a)

    import numpy as np
    a = np.array([[1,2,3],[1,5,6],[1,8,9]])
    print(a[:][0])
    from scipy import sparse
    from sklearn.preprocessing import OneHotEncoder
    ohenc = OneHotEncoder()
    # ohmat = ohenc.fit_transform(a[:,0].reshape([-1,1]))
    # for j in range(2, len(a[0])):
    #     ohmat = sparse.hstack([ohmat, ohenc.fit_transform(a[:,j].reshape([-1,1]))])
    # print(ohmat.toarray())
    ohmat = ohenc.fit_transform(a)
    print(ohmat.toarray())
    print(type(ohmat))
    print(ohenc.transform(np.array([[1,2,3], [1,8,6]])).toarray())




