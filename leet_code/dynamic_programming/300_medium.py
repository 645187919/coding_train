#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-29 20:31 
# @Author : magician 
# @File : 300_medium.py 
# @Software: PyCharm

# 300. 最长递增子序列
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
# 示例 1：
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
# 提示：
#
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104

# 思路：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/
# 参考：代码随想录

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i]:索引为i的nums包含的最长递增子序列的长度。
        #递归公式：若num[i]>num[j],j位于[0,i-1]:dp[i]=max(dp[i],dp[j]+1)
        #初始化（每个元素最小长度为1）
        len_nums=len(nums)
        dp=[1 for i in range(len_nums)]
        #遍历方向：
        for i in range(1,len_nums):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)


