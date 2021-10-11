#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-10-08 15:06 
# @Author : magician 
# @File : 322_meidum.py 
# @Software: PyCharm

# 322. 零钱兑换
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
# 你可以认为每种硬币的数量是无限的。
#
# 示例 1：
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
# 示例 2：
# 输入：coins = [2], amount = 3
# 输出：-1
# 示例 3：
# 输入：coins = [1], amount = 0
# 输出：0
# 示例 4：
#
# 输入：coins = [1], amount = 1
# 输出：1
# 示例 5：
# 输入：coins = [1], amount = 2
# 输出：2
#
#
# 提示：
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

#参考：代码随想录pdf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #确定dp[i]含义：凑够i所需要最少的硬币数。
        #递推公式：dp[i]=min(dp[i],dp[i-coins[j]]+1)
        #初始化 dp[0]=0

        dp=[float("inf") for i in range(amount+1)]
        print(dp[0]>9999)
        dp[0]=0
        #确定遍历方式：
        #遍历背包
        for i in range(1,amount+1):
            #遍历物品
            for coin in coins:
                if i>=coin:
                    dp[i]=min(dp[i],dp[i-coin]+1)

        return dp[-1] if(dp[-1]!=float("inf")) else -1