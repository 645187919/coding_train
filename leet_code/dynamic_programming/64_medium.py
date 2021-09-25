#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-25 17:04 
# @Author : magician 
# @File : 64_medium.py 
# @Software: PyCharm

# 64. 最小路径和
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
# 示例 1：
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 示例 2：
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100

#动态规划五部曲：难点在于递推公式
#参考：https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-dong-tai-gui-hua-gui-fan-liu-c/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        #dp[i][j]:第i,j单元对应的最小数字和。

        #递推公式：特殊情况，i和j非边界元素（注意边界元素为0行和0列的元素）
        #dp[i][j]=min(dp[i-1][j]+dp[i][j-1])+grid[i][j]
        #若i或j为边界元素0
        #i=0:dp[i][j]=dp[i][j-1]+grid[i][j]
        #j=0:dp[i][j]=dp[i-1][j]+grid[i][j]
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n for i in range(m)]

        dp[0][0]=grid[0][0]
        for i in range(0,m):
            for j in range(0,n):
                #递推公式
                if i==0 and j==0:
                    continue
                if i==0:
                    dp[i][j]=dp[i][j-1]+grid[i][j]
                if j==0:
                    dp[i][j]=dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[-1][-1]
