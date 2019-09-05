#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/24 10:48
# @Author   : Daishijun
# @Site     : 
# @File     : prob.py
# @Software : PyCharm

# values = list(map(int, input().split()))

inputs = list(map(int, input().split()))

target = inputs[0]
N = inputs[1]

values = inputs[2:]



# using namespace std;
# int main(){
# 	int n,x,a[30],s=0;
# 	cin>>n>>x;
# 	for(int i=0;i<n;++i)
# 	{
# 		cin>>a[i];
# 		s+=a[i];
# 	}
# 	if(s<x)
# 	{
# 		cout<<-1<<endl;
# 		return 0;
# 	}
# 	int ans=999999;
# 	for(int i=1;i<(1<<n);++i)
# 	{
# 		int t=0;
# 		for(int j=0;j<n;++j)
# 		if(i&(1<<j))
# 		{
# 			t+=a[j];
# 		}
# 		if(t>=x) ans=min(ans,t);
# 	}
# 	cout<<ans<<endl;
# 	return 0;


maxCost = 10010
def minCost(target, N, values):
    if sum(values) >= target *3  or sum(values)<target:
        return -1
    dp = [[0]*(maxCost) for _ in range(N+1)]
    for i in range(target+1):
        dp[0][i] = maxCost
    for i in range(1, N+1):
        for j in range(target+1):
            if j <= values[i-1]:
                dp[i][j] = min(values[i-1], dp[i-1][j])
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-values[i-1]]+values[i-1])
    return dp[N][target]

print(minCost(target, N, values))