#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-24 20:29 
# @Author : magician 
# @File : 343_medium.py 
# @Software: PyCharm



# 343. 整数拆分
# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
#
# 示例 1:
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
# 示例 2:
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
# 说明: 你可以假设 n 不小于 2 且不大于 58。


#详情参考：笔记代码随想录

class Solution:
    def integerBreak(self, n: int) -> int:

        #确定dp数组及其下标含义：dp[i]:将正整数i拆分得到对应的最大乘积的结果。
        #递推公式：j*(i-j)，j为0到j。

        dp=[0 for i in range(n+1)]
        dp[2]=1

        for i in range(3,n+1):
            for j in range(1,i):
                dp[i]=max(dp[i],max((i-j)*j,dp[i-j]*j))
        print(dp)
        return dp[n]


