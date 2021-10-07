#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-10-07 21:36 
# @Author : magician 
# @File : 213_meidum.py 
# @Software: PyCharm

# 213. 打家劫舍 II
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
#
# 示例 1：
#
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 示例 2：
#
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 3：
#
# 输入：nums = [0]
# 输出：0
#
#
# 提示：
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000


class Solution:
    def rob(self, nums: List[int]) -> int:
        def max_rob(nums: List[int]) -> int:
            #dp[i]：考虑偷i个房子所能拿到的最大金额；
            #状态转移方程：dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])
            #初始化：dp[0]=0,dp[1]=num[0]
            #遍历
            n_len=len(nums)

            dp=[0 for i in range(n_len+1)]
            dp[0]=0
            dp[1]=nums[0]
            for i in range(2,n_len+1):
                dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])

            return dp[-1]

        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        #从第一个房子开始抢，最后一个房子不抢。
        num1=nums[0:len(nums)-1]
        #从第二个房子开始抢，最后一个房子抢。
        num2=nums[1:]
        #比较两种情况的最大值
        return max(max_rob(num1),max_rob(num2))