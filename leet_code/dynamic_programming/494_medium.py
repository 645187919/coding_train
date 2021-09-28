#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-28 21:48 
# @Author : magician 
# @File : 494_medium.py 
# @Software: PyCharm

# 494. 目标和
# 给你一个整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
# 示例 1：
#
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 示例 2：
#
# 输入：nums = [1], target = 1
# 输出：1
# 提示：
#
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 1000

#思路：https://leetcode-cn.com/problems/target-sum/solution/494-mu-biao-he-dong-tai-gui-hua-zhi-01be-78ll/



class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sumAll = sum(nums)
        if S > sumAll or (S + sumAll) % 2:
            return 0
        if len(nums)==1 and abs(sumAll)!=abs(S):
            return 0
        target = (S + sumAll) // 2

        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] + dp[j - num]
        return dp[-1]
