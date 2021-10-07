#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-23 20:30 
# @Author : magician 
# @File : 63_medium.py 
# @Software: PyCharm




class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #新建矩阵版
        height, width = len(obstacleGrid),len(obstacleGrid[0])
        #注意初始化矩阵的写法
        store = [[0]*width for i in range(height)]

        #从上到下，从左到右
        for m in range(height):#每一行
            for n in range(width):#每一列
                if not obstacleGrid[m][n]: #如果这一格没有障碍物
                    if m == n == 0: #或if not(m or n)
                        store[m][n] = 1
                    else:
                        a = store[m-1][n] if m!=0 else 0 #上方格子
                        b = store[m][n-1] if n!=0 else 0 #左方格子
                        store[m][n] = a+b
        return store[-1][-1]


#若遇到障碍，则将其dp值设为0。若在0行0列遇到障碍，则其后面的dp值全部为0。
#也可以初始化每个dp值为0,然后将dp[0][0]初始化为1，这样就避免遇到障碍物时将其后面的dp值全部设置为0的处理。
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        #dp[i][j]：到该位置有多少条不同的路径
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])


        #递推公式：dp[i][j]=dp[i-1][j]+dp[i][j-1]  #前提条件，非0行0列的节点，且该节点不为障碍物。
        #若节点为障碍物，则dp[i][j]=0(即初始位置到障碍物有0条路径)
        #若节点为0行0列的节点，则dp[i][j]=1,注意若障碍物后面，则全部为0。

        dp=[[1]*n for i in range(m)]

        #初始化:将0列和0行中障碍物后面的dp值都设置为0。
        #(0列)
        for i in range(m):
            if obstacleGrid[i][0]==1 :
                while i<m:
                    dp[i][0]=0
                    i+=1
                break
        #0行
        for i in range(n):
            if obstacleGrid[0][i]==1 :
                while i<n:
                    dp[0][i]=0
                    i+=1
                break

        print(dp)
        #遍历方向：
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    continue
                else:
                    if obstacleGrid[i][j]==1:
                        dp[i][j]=0
                    else:
                        dp[i][j]=dp[i-1][j]+dp[i][j-1]
        print(dp)
        return dp[-1][-1]