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
        #1、dp[i][j]:走到该节点处的最小路径
        #注意如何生成矩形的数组
        len_grid=len(grid)
        len_col=len(grid[0])
        dp=[[0]*len(grid[n]) for n in range(len_grid)]
        #2、确定递推方程：
        #i和j没有位于首行或首列：dp[i][j]=min(dp[i-1][j]+grid[i][j],dp[i][j-1]+grid[i][j])
        #i和j位于首行或首列：dp[i][j]=dp[i-1][j]+grid[i][j] or dp[i][j-1]+grid[i][j]
        # #(里面的所有坐标是有效的)
        #3、初始化：dp[0][0]=grid[0][0]
        #4、遍历方向：

        for i in range(len_grid):
            for j in range(len_col):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                elif i==0:
                    dp[i][j]=dp[i][j-1]+grid[i][j]
                elif j==0:
                    dp[i][j]=dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j]+grid[i][j],dp[i][j-1]+grid[i][j])
        return dp[-1][-1]

