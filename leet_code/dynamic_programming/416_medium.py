#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-24 21:50 
# @Author : magician 
# @File : 416_medium.py 
# @Software: PyCharm
# 416. 分割等和子集
# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 示例 1：
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
# 示例 2：
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
# 提示：
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100

#思路：将该问题转化为背包问题


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        #3、初始化
        dp=[0 for i in range(10001)]
        #1、确定dp[i]：背包总容量为i时，可以凑成i的最大的子集总和为dp[i]
        #获取总和
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
        if (sum%2==1):
            return False
        target=sum//2
        #4、确定遍历
        for i in range(len(nums)):
            for j in range(target,-1,-1):
                if j>=nums[i]:
                    #2、递推公式
                    dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])

        if dp[target]==target:
            return True
        return False

