#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-21 15:36 
# @Author : magician 
# @File : leetcode_509.py 
# @Software: PyCharm

# 509. 斐波那契数
# 斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
# 给你 n ，请计算 F(n) 。
# 示例 1：
# 输入：2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1
# 示例 2：
# 输入：3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2
# 示例 3：
# 输入：4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3
# 提示：
# 0 <= n <= 30

#思路：1、递归；2、通过备忘录或db table 来解决重复子问题；3、动态规划


class Solution:
    #方法1：暴力解法
    def fib(self, n: int) -> int:
        #暴力解法：递归
        if n==0:
            return 0
        if n==1:
            return 1

        return self.fib(n-1)+self.fib(n-2)

    #方法2：使用缓存即备忘录（db table）来解决重叠子问题
    @functools.lru_cache(None)#关于该函数资料请参考：https://blog.csdn.net/Victor_Monkey/article/details/80524571
    #该函数功能，将该方法的入参和结果存入缓存，若二次调用，则直接从缓存中取结果，省去计算过程！
    def fib(self, n: int) -> int:
        #使用缓存即备忘录（db table）来解决重叠子问题
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)

    #方法三：#动态规划：自底向上
    def fib(self, n: int) -> int:

        if n<=1:
            return n
        else:
            #动态规划
            dp=['-1']*(n+1)
            #base case
            dp[0],dp[1],dp[2]=0,1,1
            for i in range(3,n+1):
                dp[i]=dp[i-1]+dp[i-2]
            return dp[n]

