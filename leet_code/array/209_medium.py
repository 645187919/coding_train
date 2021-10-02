#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/9 16:51 
# @Author : magician 
# @File : 209_medium.py 
# @Software: PyCharm


# 209. 长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，
# 并返回其长度。如果不存在符合条件的子数组，返回 0。

# 示例：
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。

# 进阶：
# 如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        #极端条件：
        if sum(nums)==s:
            return len(nums)
        elif sum(nums)<s:
            return 0

        #窗口指针的思想
        #声明左指针和子数组的和
        tmp_sum=left=0
        #满足条件的最小子数组长度
        min_length=len(nums)
        #右指针开始滑动
        for right in range(len(nums)):
            #对左右指针包括的数组元素进行累加
            tmp_sum+=nums[right]
            #判断子数组是否满足条件
            while tmp_sum>=s:
                #比较子串与原有最小长度的大小。
                min_length=min(min_length,right-left+1)
                #对子串进行裁剪。看是否依旧满足>=s的条件（已知右指针对应的value值满足要求后，
                # 需要针对左指针对应的value值即未知情况进行排除！）
                tmp_sum-=nums[left]
                left+=1

        return min_length


#20211001 新实现
# 参考：https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/hua-dong-chuang-kou-on-er-fen-fa-onlogn-by-powcai/
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        nums_len=len(nums)
        #特殊情况
        if sum(nums)<target:
            return 0
        if sum(nums)==target:
            return nums_len
        tmp_total=0
        #滑动窗口的左索引
        left=0
        result=float("inf")
        #滑动窗口的右索引
        for right in range(nums_len):
            #元素的累加值
            tmp_total+=nums[right]
            #若当前窗口的累加值满足条件，则求最小的长度，并剔除左索引值后，再循环判断。
            while  tmp_total>=target:
                result=min(result,right-left+1)
                tmp_total-=nums[left]
                left+=1
        return result
