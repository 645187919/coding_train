#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-22 21:38 
# @Author : magician 
# @File : 62_medium.py 
# @Software: PyCharm





class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp=[[1]*n for i in range(m)]
        #递推公式：dp[i][j]=dp[i-1][j]+dp[i][j-1] #非0行0列的情况
        #dp[i][j]=1 #0行0列的情况。
        #初始化：0行0列的值都为1。
        #遍历方式：
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    continue
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        #观察dp
        print(dp)
        return dp[-1][-1]




