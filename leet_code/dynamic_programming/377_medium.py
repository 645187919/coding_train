#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-27 21:21 
# @Author : magician 
# @File : 377_medium.py 
# @Software: PyCharm

# 377. 组合总和 Ⅳ
# 给你一个由不同整数组成的数组 nums ，和一个目标整数 target 。
# 请你从 nums 中找出并返回总和为 target 的元素组合的个数。
# 题目数据保证答案符合 32 位整数范围。
# 示例 1：
#
# 输入：nums = [1,2,3], target = 4
# 输出：7
# 解释：
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。
# 示例 2：
#
# 输入：nums = [9], target = 3
# 输出：0
#
#
# 提示：
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# nums 中的所有元素 互不相同
# 1 <= target <= 1000

#思路：https://leetcode-cn.com/problems/combination-sum-iv/solution/xi-wang-yong-yi-chong-gui-lu-gao-ding-bei-bao-wen-/
#参考代码随想录
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #dp[i]:凑成目标为i的元素组合的个数
        dp=[0 for i in range(target+1)]
        #递推公式：dp[i]+=dp[i-nums[j]]
        #初始化：dp[0]=1
        dp[0]=1
        #遍历
        for i in range(1,target+1):
            for j in range(len(nums)):
                if i>=nums[j]:
                    dp[i]+=dp[i-nums[j]]
        # print(dp)
        return dp[-1]
