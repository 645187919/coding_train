#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-10-04 16:52 
# @Author : magician 
# @File : leetcode_279.py 
# @Software: PyCharm

# 279. 完全平方数
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
# 你需要让组成和的完全平方数的个数最少。
# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
# 例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#
# 示例 1：
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4
# 示例 2：
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
#
# 提示：
#
# 1 <= n <= 104

#思路：动态规划，
# 参考：代码随想录。转化为背包问题

class Solution:
    def numSquares(self, n: int) -> int:
        if n<=3:
            return n
        # 1、确定dp[i]的含义：正整数i差分成多个完全平方数的数组的最小长度。
        dp=[99999 for i in range(n+1)]
        #2、确定递推公式：dp[i]=min(dp[i],dp[i-j*j]+1)。j=i的平方根。
        #3、初始化.dp[1]=1,dp[2]=2
        dp[0],dp[1],dp[2]=0,1,2
        #4、确定遍历方式：
        for i in range(3,n+1):
            for j in range(1,int(i**0.5)+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
        #5、确定dp结果
        print(dp)
        return dp[-1]