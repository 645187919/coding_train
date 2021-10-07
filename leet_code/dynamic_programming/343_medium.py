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
        #1、确定dp[i]数组含义：正整数i拆分成两个正整数的最大乘积为dp[i]
        dp=[0 for i in range(n+1)]
        #2、确定递推公式：两种方法得到dp[i]，1、dp[i-j]*j；2、(i-j)*j
        # dp[i]=max(dp[i-j]*j,(i-j)*j)
        #3、初始化：dp[2]=1;
        dp[2]=1
        #4、确定遍历方向：

        for i in range(3,n+1):
            for j in range(1,i):
                #由于每次从0到i的迭代都会生成一个dp[i]，所以还需要对多个dp[i]进行比较，挑选出最大的那一个！
                #所以最终的公式为：dp[i]=max(dp[i],max(dp[i-j]*j,(i-j)*j))
                dp[i]=max(dp[i],max(dp[i-j]*j,(i-j)*j))
        return dp[-1]


