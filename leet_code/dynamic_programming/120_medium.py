#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-25 16:25 
# @Author : magician 
# @File : 120_medium.py 
# @Software: PyCharm


# 120. 三角形最小路径和
# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
# 每一步只能移动到下一行中相邻的结点上。相邻的结点在这里指的是下标与上一层结点下标相同或者等于
# 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i
# 或 i + 1 。
#
# 示例 1：
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
# 2
# 3 4
# 6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 示例 2：
# 输入：triangle = [[-10]]
# 输出：-10
#
#
# 提示：
#
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104

#思路：考虑每层的首尾元素得特殊处理。自顶向下，每个元素的dp值等于上层相邻的元素的dp值+该元素的值
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #1、确认dp数组:dp[i][j]最小的路径和；
        #注意如何生成矩阵（三角形）的dp数组
        dp=[[0]*len(triangle[row])  for row in range(len(triangle))]
        #2、确定递推方程：
        #i,j不为边界索引：dp[i][j]=min(dp[i-1][j]+triangle[i][j],dp[i-1][j-1]+triangle[i][j])
        #i,j为边界索引：dp[i][j]=dp[i-1][j]++triangle[i][j]

        #3、初始值；dp[i][j]=triangle[i][j]
        #4、遍历方式：
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i==0 and j==0:
                    dp[i][j]=triangle[i][j]
                elif j==0:
                    print(i,j)
                    dp[i][j]=dp[i-1][j]+triangle[i][j]
                elif i==j:
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j]+triangle[i][j],dp[i-1][j-1]+triangle[i][j])
        return min(dp[-1])








