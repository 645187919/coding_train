#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-24 20:40 
# @Author : magician 
# @File : 96_medium.py 
# @Software: PyCharm

# 96. 不同的二叉搜索树
# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
# 示例 1：
# 输入：n = 3
# 输出：5
# 示例 2：
# 输入：n = 1
# 输出：1
#
# 提示：
# 1 <= n <= 19

#思路：参考笔记代码随想录


class Solution:
    def numTrees(self, n: int) -> int:
        #dp[n]:n个节点能够生成多少种不同的二叉搜索树
        #递推公式：dp[i] += dp[j - 1] * dp[i - j]
        dp=[0 for i in range(n+1)]

        dp[0]=1

        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]