#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-22 21:38 
# @Author : magician 
# @File : 62_medium.py 
# @Software: PyCharm





class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        #dp数组代表第i*j的网格有多少条路径
        #构造m*n的矩阵
        dp_1=[-1]*n
        dp=[dp_1]*m


        #初始化，当处于0行或者0列时，对应的路径只有1条
        for i in range(m):
            for j in range(n):
                if j==0 or i==0:
                    dp[i][j]=1
        #递推公式
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        #返回重点值。注意是m-1和n-1
        return dp[m-1][n-1]




