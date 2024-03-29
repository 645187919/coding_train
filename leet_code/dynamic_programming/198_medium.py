#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-26 21:13 
# @Author : magician 
# @File : 198_medium.py 
# @Software: PyCharm

# 198. 打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
# 影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，
# 系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你不触动警报装置的情况下 ，
# 一夜之内能够偷窃到的最高金额。
#
# 示例 1：
#
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2：
#
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

#参考：https://leetcode-cn.com/problems/house-robber/solution/dong-tai-gui-hua-jie-ti-si-bu-zou-xiang-jie-cjavap/

# 参考：代码随想录
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return max(nums)
        #dp[i]：考虑偷i间房子所能拿到的最大金额；
        dp=[0 for i in range(n+1)]
        #状态转移方程：dp[i]=max(dp[i-2]+nums[i],dp[i-1])

        #dp数组初始化；
        dp[1]=nums[0]
        dp[2]=max(nums[0],nums[1])
        print(dp)
        for i in range(2,n+1):
            dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
        print(dp)
        return max(dp)
