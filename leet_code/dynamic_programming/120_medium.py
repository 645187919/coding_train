#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-25 16:25 
# @Author : magician 
# @File : 120_medium.py 
# @Software: PyCharm


# 120. 三角形最小路径和
# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
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
# 详情参考：https://leetcode-cn.com/problems/triangle/solution/san-jiao-xing-zui-xiao-lu-jing-he-by-leetcode-solu/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m, n = len(triangle),len(triangle[-1])
        #1、dp[i][j]:代表自顶向下走到i行j列对应的最小路径和。
        dp=[[0]*n for i in range(m)]
        #3、初始化：dp[0][0]=triangle[0][0]
        #特殊情况
        if m==1:
            return triangle[0][0]
        #所以初始值都设置为负无穷大
        dp[0][0]=triangle[0][0]
        dp[1][0]=triangle[0][0]+triangle[1][0]
        dp[1][1]=triangle[0][0]+triangle[1][1]

        #4、确定遍历方向
        for i in range(2,m):
            #2、递推公式：
            #每层的首元素
            dp[i][0]=dp[i-1][0]+triangle[i][0]
            for j in range(1,len(triangle[i])):
                #每层的末尾元素的处理
                if j==len(triangle[i])-1:
                    dp[i][j]=triangle[i][j]+dp[i-1][j-1]
                else:
                    dp[i][j]=triangle[i][j]+min(dp[i-1][j],dp[i-1][j-1])
        return min(dp[-1])

